import telepot
from pprint import pprint
from telepot.loop import MessageLoop
import time 
from newsBot import newsBot
from covidStatsBot import covidStatsBot

def explanation(chat_id):
    bot.sendMessage(chat_id, 'Now you can use 3 modes:\n'
                            '1. "1, website, 20", where 1 is the mode, site is the site, for example, "bloomberg.com", 20 is the number of recent news.\n'
                            '2. "2, something, 20", where 2 is the mode, something is interesting topic for you, for example, "economy", 20 is the number of recent news.\n'
                            '3. "3, something, website, 20", you can read about all components above.\n'
                            '4. "4, country", where 4 is the mode, country is the country you want information about. If you want to get global ifno write "4, None"\n'
                            'If you want to get news - write one of these lines to me!')

def sendNews(chat_id, news):
    for curNews in news:
        bot.sendMessage(chat_id, curNews, disable_web_page_preview=True)

def sendStats(chat_id, stats):
    for stat in stats:
        bot.sendMessage(chat_id, stat)

def checkMsg(chat_id, message):
    message = message.split(',')
    try:
        #curNews = newsBot(message[1], int(message[2]))
        flag = 1
        if message[0] == '1':
            curNews = newsBot(None, message[1].strip(), int(message[2]))
            curNews.firstMode()
        elif message[0] == '2':
            curNews = newsBot(message[1].strip(), None, int(message[2]))
            curNews.secondMode()
        elif message[0] == '3':
            curNews = newsBot(message[1].strip(), message[2].strip(), int(message[3]))
            curNews.thirdMode()
        elif message[0] == '4':
            curStats = covidStatsBot(message[1].strip())
            curStats.getData()
            data = curStats.outPutData()
            sendStats(chat_id, data)
            flag = 2
        else:
            flag = 0
        if flag == 1:
            curNews.getNews()
            news = curNews.outPutData()
            sendNews(chat_id, news)
        elif flag != 2:
            bot.sendMessage(chat_id, 'Your line was wrong!')
            explanation(chat_id)
    except Exception as e:
        print(e)
        bot.sendMessage(chat_id, 'We could not find anything or your line was wrong!')
        explanation(chat_id)

def scanIdFromFile():
    idForSave = []
    f = open('id.txt', 'r')
    for line in f:
        idForSave.append(int(line))
    return idForSave

def writeAllIds(idForSave):
    for id in idForSave:
        bot.sendMessage(id, 'The bot was rebooted, so if you wrote something, write again!')

def on_chat_message(msg):
    chat_id = msg['chat']['id']
    if chat_id not in idForSave:
        idForSave.append(chat_id)
    message = msg['text']
    checkMsg(chat_id, message)

def newFeatures(idForSave):
    for id in idForSave:
        bot.sendMessage(id, 'We did some fixes, now you can use all modes.')


try:
    if __name__ == "__main__":
        idForSave = scanIdFromFile()
        TOKEN = 'YOUR TOKEN'
        basic_auth = ('LOGIN', 'PASSWORD')
        telepot.api.set_proxy("YOUR PROXY", basic_auth)
        bot = telepot.Bot(TOKEN)
        writeAllIds(idForSave)
        newFeatures(idForSave)
        MessageLoop(bot, {'chat': on_chat_message}).run_as_thread()
    while 1:
        time.sleep(10)
except:
    print(idForSave)
    f = open('id.txt', 'w')
    for id in idForSave:
        f.write(str(id))
    f.close()

#subject = str(input('Введите тему > '))
#countOfLastNews = int(input('Введите количество последних новостей (до 20) > '))
#userID = None
#bot = newsBot(subject=subject, countOfLastNews=countOfLastNews, userID=userID)
#bot.getNews()
