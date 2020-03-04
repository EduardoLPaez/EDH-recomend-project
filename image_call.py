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

def get_img(url):
    sleep(.01)
    get_ = requests.get(url)
    json_ = json.loads(get_.text)
    return json_['image_uris']['normal']



# will return entirety of card list ready to call in scryfall
return_ = [f'{scryfall_end}/cards/{i}' for i in df]

# calls all of them, and returns the uri for all images.   
img_uri = pd.DataFrame(data = [get_img(i) for i in return_], columns = 'img_uris')

img_uri.to_csv('Images/img_uri.csv', index = False)