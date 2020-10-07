import urllib.request, urllib.parse, urllib.error
import json

class covidStatsBot():
    def __init__(self, country):
        self.country = country
        self.url = 'https://api.covid19api.com/summary'
        self.data = None
        self.globalData = None

    def getData(self):
        self.data = (json.loads(urllib.request.urlopen(self.url).read().decode()))
        self.globalData = self.data['Global']
        #print(self.globalData)
        self.data = self.data['Countries']

    def findIndex(self):
        index = None
        for i in range(len(self.data)):
            if self.data[i]['Country'] == self.country:
                index = i
                return index
            elif self.data[i]['CountryCode'] == self.country:
                index = i
                return index
            elif self.data[i]['Slug'] == self.country:
                index = i
                return index
        return index

    def appendGlobal(self):
        string = ''
        string = '' + 'Global information\n'
        string += 'New confirmed = ' + str(self.globalData['NewConfirmed']) + '\n'
        string += 'Total Confirmed = ' + str(self.globalData['TotalConfirmed']) + '\n'
        string += 'New Deaths = ' + str(self.globalData['NewDeaths']) + '\n'
        string += 'Total Deaths = ' + str(self.globalData['TotalDeaths']) + '\n'
        string += 'New Recovered = ' + str(self.globalData['NewRecovered']) + '\n'
        string += 'Total Recovered = ' + str(self.globalData['TotalRecovered']) + '\n\n'
        return string

    def appendForCountry(self, i):
        string = '' + str(self.data[i]['Country']) + ' information\n'
        string += 'New confirmed = ' + str(self.data[i]['NewConfirmed']) + '\n'
        string += 'Total Confirmed = ' + str(self.data[i]['TotalConfirmed']) + '\n'
        string += 'New Deaths = ' + str(self.data[i]['NewDeaths']) + '\n'
        string += 'Total Deaths = ' + str(self.data[i]['TotalDeaths']) + '\n'
        string += 'New Recovered = ' + str(self.data[i]['NewRecovered']) + '\n'
        string += 'Total Recovered = ' + str(self.data[i]['TotalRecovered']) + '\n\n'
        return string

    def outPutData(self):
        newData = []
        newData.append(self.appendGlobal())
        index = self.findIndex()
        if index != None:
            newData.append(self.appendForCountry(index))
        return newData
        


