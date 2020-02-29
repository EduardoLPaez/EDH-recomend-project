import pandas as pd
import numpy as np
import re
import sqlite3

connect = sqlite3.connect('AllPrintings.sqlite')


# pipeline for optiyzation, 
def clean():
    data = pd.read_sql_query( 
    # will ned to pull name, rules text, cost, colosr, converted cost, type, types, 
    """SELECT * 
    FROM cards
    WHERE borderColor IS 'black' 
    """
    , connect)
    # make cleaning 
    data = deep_clean(data)
    return data

def deep_clean(data):
    data2 = data[['name', 'names', 'power', 'toughness', 'text',
     'type', 'types', 'subtypes', 'supertypes', 'rarity', 'colorIdentity', 'colors',
      'convertedManaCost', 'manaCost', 'faceConvertedManaCost',  'side', ]]
    data2 = color_split(data2)


    return data2

def color_split(data): # creates a get dummies for color cost and color identity, also drops new useless columns.
    names = ['Green','Blue','Black','Red','White']
    start_ = ['G','U','B','R','W']

    for i,el in enumerate(names): # creates columns with cost of colors and color identity
        # color cost VV
        data[f'manaCost_{el}'] = data['manaCost'].apply(lambda x: str(x).count(f'{start_[i]}'))
    # bellow gennerates cost of colorless. 
    data['manaCost_colorless'] = data['convertedManaCost'].astype('int') - sum(
        [data['manaCost_Green'],
        data['manaCost_Red'],
        data['manaCost_Black'],
        data['manaCost_Blue'], 
        data['manaCost_White']
        ])

    # color identity VV
    for i,el in enumerate(names):
        data[f'colorIdentity_{el}'] = data['colorIdentity'].apply(lambda x: str(x).count(f'{start_[i]}'))
    # bellow generates column for colorless identity
    data['colorIdentity_colorless'] = [1 if x == True else 0 for x in data['colorIdentity'].isna()]

    data.drop(columns = ['manaCost','colors','colorIdentity'], inplace = True)
    return data

try:
    data = pd.read_csv('mtg_modern_clean.csv')
except:
    data = clean()