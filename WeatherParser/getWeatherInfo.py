import urllib.request, urllib.parse, urllib.error
import json
import requests
import sys  
from PyQt5 import QtWidgets  
import designWeather  

def translateWord(word):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?' 
    key = 'trnsl.1.1.20190227T075339Z.1b02a9ab6d4a47cc.f37d50831b51374ee600fd6aa0259419fd7ecd97'  
    lang = 'ru-en' 
    r = requests.post(url, data={'key': key, 'text': word, 'lang': lang}) 
   
    return json.loads(r.text)['text'][0]

class weatherFind(QtWidgets.QMainWindow, designWeather.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.urlStart = 'http://api.openweathermap.org/data/2.5/find?q='
        self.urlEnd = '&APPID=' + 'API KEY' + '&units=metric'
        self.find.clicked.connect(self.checkCity)
        self.endResult = None

    def outputInfo(self, curTemp, curFeel, curTempMax, curTempMin, curPressure, curResult):
        self.tempOut.setText(str(curTemp))
        self.feelOut.setText(str(curFeel))
        self.maxTempOut.setText(str(curTempMax))
        self.minTempOut.setText(str(curTempMin))
        self.pressureOut.setText(str(curPressure))
        self.resultOut.setText(str(curResult))

    def checkCity(self):
        try:
            city = self.lineEdit.text()
            url = self.urlStart + translateWord(city) + self.urlEnd
            data = urllib.request.urlopen(url).read().decode()
            data = json.loads(data)
            curTemp = data['list'][0]['main']['temp']
            curFeel = data['list'][0]['main']['feels_like']
            curTempMax = data['list'][0]['main']['temp_max']
            curTempMin = data['list'][0]['main']['temp_min']
            curPressure = data['list'][0]['main']['pressure']
            curResult = 'Верно'
        except:
            curTemp = ''
            curFeel = ''
            curTempMax = ''
            curTempMin = ''
            curPressure = ''
            curResult = 'Неверно'
        self.outputInfo(curTemp, curFeel, curTempMax, curTempMin, curPressure, curResult)


def main():
    app = QtWidgets.QApplication(sys.argv) 
    window = weatherFind()  
    window.show()  
    app.exec_() 

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main() 