import urllib.request, urllib.parse, urllib.error
import json

class newsBot():
    def __init__(self, subject, website, countOfLastNews):
        self.subject = subject
        self.countOfLastNews = countOfLastNews
        self.data = None
        self.website=website
        self.url = None

    def firstMode(self):
        apiKey = 'YOUR API KEY'
        url = 'http://newsapi.org/v2/everything?domains=' + self.website + '&apiKey=' + apiKey
        self.url = url

    def secondMode(self):
        apiKey = 'YOUR API KEY'
        url = 'http://newsapi.org/v2/everything?q=' + self.subject + '&apiKey=' + apiKey
        self.url = url
    
    def thirdMode(self):
        apiKey = 'YOUR API KEY'
        url = 'http://newsapi.org/v2/everything?q=' + self.subject +  '&domains=' + self.website + '&apiKey=' + apiKey
        self.url = url

    def getNews(self):
        self.data = (json.loads(urllib.request.urlopen(self.url).read().decode()))
        self.data = self.data['articles'][:self.countOfLastNews]

    def outPutData(self):
        newData = []
        for item in self.data:
            string = ''
            string += 'Magazine: ' + item['source']['name'] + '\n'
            string += item['title'] + '\n'
            if item['description'] != None:
                string += item['description'] + '\n'
            string += 'If you want to see more information go to: ' + item['url']
            newData.append(string)
        return newData