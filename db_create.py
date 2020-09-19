# purpose is to get the base db of all cards, intended plans are to have the pull from mtgjson.com 
# then make an automation to check current date from the date of last pull, if in exes of 3-4 months
# then it pulls the most current ersion and re runs the clean.py section.
import pandas as pd
import numpy as np
import os.path, time
from datetime import datetime
import requests


# last time modified is0: os.path.ctime(), time interval is gonna be slated to be 3-4 months(likely 4)
# this is to permit blcok rotation. return is in unix time.
def date_chek():
    last_mod = datetime.utcfromtimestamp(os.path.getmtime('AllPrintings.sqlite'))# works, 
    current = datetime.utcnow()#gets curent date.

    if (current - last_mod).days >= 90:
        return True
    else:
        return False

def db_core_pull():
    if date_chek() == True:
        # pull from origin... need some time for this...
        responce = requests.get('http://mtgjson.com/api/v5/AllPrintings.json')
        # print(responce.json())
        # test = pd.read_sql(responce)
        # test.head(1)
    else:
        return

db_core_pull()
# bellow is creation time, -----to add to tollbelt later----- 
# print("created: %s" % time.ctime(os.path.getctime('AllPrintings.sqlite')))
