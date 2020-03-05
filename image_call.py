# this code is for converitng scryfall image ids into an html direction
# all images are owned by wizards of the coast. 
import pandas as pd
import numpy as np
import requests
from time import sleep
import json

scryfall_end = 'https://api.scryfall.com'
frame = pd.read_csv('mtg_modern_clean.csv')
df = frame['scryfallId'] #.astype('list')

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def get_img(url, iter):
    sleep(.0050)
    get_ = requests.get(url)
    json_ = json.loads(get_.text)
    printProgressBar(iter, len(return_))
    try:
        return json_['image_uris']['normal'] 
    except:
        return None




# will return entirety of card list ready to call in scryfall
return_ = [f'{scryfall_end}/cards/{i}' for i in df]

# calls all of them, and returns the uri for all images.   
list_ = [get_img(el,i) for i,el in enumerate(return_)]
img_uri = pd.DataFrame(data = list_)

img_uri.to_csv('Images/img_uri.csv')