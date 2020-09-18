# purpose is to get the base db of all cards, intended plans are to have the pull from mtgjson.com 
# then make an automation to check current date from the date of last pull, if in exes of 3-4 months
# then it pulls the most current ersion and re runs the clean.py section.
import pandas as pd
import numpy as np
import os.path, time
from datetime import datetime 

now = datetime.now() # redundancies are grand arent they....

# last time modified is0: os.path.ctime(), time interval is gonna be slated to be 3-4 months(likely 4)
# this is to permit blcok rotation. return is in unix time.
"last modified: %s" % time.ctime(os.path.getmtime('AllPrintings.sqlite'))# works, 
print(now.strftime("%D"))#gets curent date.

# bellow is creation time, -----to add to tollbelt later----- 
# print("created: %s" % time.ctime(os.path.getctime('AllPrintings.sqlite')))
