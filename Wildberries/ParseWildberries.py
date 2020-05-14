import requests # Модуль для обработки URL
from lxml import etree
import lxml.html
import csv


class ParseWildberries():
    def __init__(self, subject, company):
        self.subject = subject
        self.company = company
        self.url = 'https://www.wildberries.ru/catalog/0/search.aspx?subject=151&search=' + self.subject + '&sort=popular'
        self.headers = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'}
        self.result = None
        
    def getInfo(self):
        api = requests.get(self.url)
        tree = lxml.html.document_fromstring(api.text)
        
        brandNum = 1
        while True:
            try:
                curBrand = (tree.xpath(f'/html/body/div[2]/div/div/div[1]/div[2]/div[6]/div[{brandNum}]/span/span/span/a/div[2]/div[3]/strong/text()'))[0].strip()
                if curBrand == self.company:
                    self.result = brandNum
                    break
                brandNum += 1
            except:
                break
        return self.result

subject = str(input('Введите ваш товар: '))
brand = str(input('Введите ваш бренд: '))
obj = ParseWildberries(subject, brand)
res = obj.getInfo()
if res:
    print("Ваш бренд находится на " + str(res) + " месте!")
else:
    print("Ваш бренд не найден.")