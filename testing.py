import redis
import logging
import json
import datetime
import re
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from textblob import TextBlob as tb
import urllib
from selenium import webdriver
from time import sleep
import threading
from random import randint


url_patern = 'http://tappedout.net/mtg-decks/'

def set_up(str_in):
    str1 = re.sub(' ', '-',str_in)
    str2 = re.sub('[\',]','',str1)
    return str2.lower()

def get_names():
    df = pd.read_csv('mtg_modern_clean.csv')
    com = df.query('is_commander == True')['name']
    weird = []
    for i in com :
        weird.append(set_up(str(i)))
    return weird

def clean(t_list):# cleaning up the name html.
    list_=[]
    for i in t_list:
        list_.append(strip_(str(i)))
    return list_
    
def strip_ (text_):# used in the above .
    step1 = re.sub('<a href="','',text_)
    step1 = re.sub('"','',step1)
    step2 = step1.split()
    step3 = step2[0]
    return step3


def parser_deck_names(in_,di, pg_num = 1): # content parser.
    
    if pg_num == 1:
        url_comm = f'https://tappedout.net/mtg-decks/search/?q=&format=edh&general={in_}&price_0=&price_1=&o=-rating&submit=Filter+results'
    elif pg_num >= 2:
        url_comm = f'https://tappedout.net/mtg-decks/search/?q=&format=edh&general={in_}&is_top=on&price_0=&price_1=&o=-date_updated&submit=Filter+results&p={pg_num}&page={pg_num}'
    
    di.get(url_comm)
    request = di.execute_script("window.scrollTo(0,document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    sleep(randint(6,8))# currently set to 4 secs(rough estimate 3600 secs.(~3h)) will need paraleles...

    returns = bs(di.page_source, 'html.parser')
    if pg_num == 1:
        page_n = parser_pgnum(returns)
    results = returns.findAll('a', title = re.compile('mtg decks -'))
    fresults = clean(results)
    return fresults, page_n

def parser_pgnum(input_):# parser to find number of pgs.
    result = input_.findAll('a',attrs = {'class':'pg-btn'})
    print(result)
    return result

class spider_Thread(threading.Thread):
    def __init__(self, com_names):
        threading.Thread.__init__(self) 
        self.com_names = com_names
        self.driver = webdriver.Firefox(executable_path=r'/home/ed/Documents/gecko/geckodriver-v0.26.0-linux64/geckodriver')
        self.list_ = []

    def run(self):
        # driver = webdriver.Firefox(executable_path=r'/home/ed/Documents/gecko/geckodriver-v0.26.0-linux64/geckodriver')
        for i in self.com_names:
            temp, pgn = parser_deck_names(i, self.driver)
            self.list_.append(temp)
        list1 = self.list_ 
        self.driver.quit()
        return list1



# list1 =[]
# for i in deck_names:
#     temp, pgn = parser_deck_names(i)
#     list1.append(temp)
    # print(pgn)
deck_names = get_names()
thread1 = spider_Thread(deck_names[:150])
thread2 = spider_Thread(deck_names[150:300])
thread3 = spider_Thread(deck_names[300:450])
thread4 = spider_Thread(deck_names[450:600])
thread5 = spider_Thread(deck_names[600:750])
thread6 = spider_Thread(deck_names[750:-1])


deck_names_complete = thread1.run()+ thread2.run() + thread3.run() + thread4.run() + thread5.run() + thread6.run()
df = pd.DataFrame(deck_names_complete)
df.to_csv('commander_deck_names.csv')
