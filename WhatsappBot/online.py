from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

# Mesajları dosyadan oku
with open('messages.txt', 'r', encoding='utf-8') as messages:
    messageList = list()
    text = messages.read()
    messageList = text.split('\n')
    
def start():
    flag = False
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get('https://web.whatsapp.com/')
    input('QR okuma işlemini gerçekleştirdikten sonra bir harf girip enterlayınız..')
    
    message_area = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
    
    while True:
        message_area.click()
        wp_source = driver.page_source
        soup = bs(wp_source, 'lxml')
        search = soup.find_all('div', {'class' : ['x78zum5 x1cy8zhl xisnujt x1nxh6w3 xcgms0a x16cd2qt']})
        try:
            online = search[0].span.text
            print(online)
            if (online in ['çevrimiçi', 'online']) and flag == False:
                print("Online")
                msgToSend = messageList[random.randint(0, len(messageList)-1)]
                message_area.send_keys(msgToSend)
                message_area.send_keys(Keys.ENTER)
                flag = True
            else:
                print("Şu anda çevrimdışı")
                flag = False
        except:
            print('Şu anda çevrimdışı hata')
            flag = False
        time.sleep(5)
        
start()
