from selenium import webdriver
from bs4 import BeautifulSoup
import time
import random


#bilgiler
adres=input("Lütfen sohbet url'sini giriniz: ")
kelime=input("Lütfen cekilis kelimesini giriniz: ")
ytLiveChatURL = adres
keyword = kelime
eligibleUsers = set()

# start web browser
tercih=input("Tarayıcı secim\n 1:Chrome \n 2:Firefox \ntercihiniz: ")
if(tercih=="1"):
    browser = webdriver.Chrome()
else:
    browser = webdriver.Firefox()


def getHTML(url):
   # get source code
    browser.get(ytLiveChatURL)
    time.sleep(1)
    page_source = browser.page_source
    return page_source


def parseHTML(html_source):
    return BeautifulSoup(html_source, 'html.parser')


def getMessages(soup):
    return soup.find_all("yt-live-chat-text-message-renderer")


def updateEligibleUsers(messages):
    for message in messages:
        content = message.find("div", {"id": "content"})
        author = content.find("span", {"id": "author-name"}).text
        message_content = content.find("span", {"id": "message"}).text
        if keyword in message_content.lower():
            eligibleUsers.add(author)


def startDrawing(eligibleUsersList):
    print("Cekilis basliyor! {totalUserCount} kisi hak kazandi.".format(
        totalUserCount=len(eligibleUsersList)))

    time.sleep(3)
    for i in range(1, 5):
        noktalar = i * "."
        print("Rasgele bir sayi cekiliyor" + noktalar)
        time.sleep(1.5)

    print("{totalUserCount} kisi arasindan kazanan:".format(
        totalUserCount=len(eligibleUsersList)), random.choice(eligibleUsersList))


def main():
    for i in range(0, 7):
        html_source = getHTML(ytLiveChatURL)
        soup = parseHTML(html_source)
        messages = getMessages(soup)
        updateEligibleUsers(messages)
        print("{count} kisi cekilise katilmis durumda.".format(
            count=len(eligibleUsers)))
        time.sleep(10)

    eligibleUsersList = list(eligibleUsers)
    startDrawing(eligibleUsersList)
    browser.close()


main()