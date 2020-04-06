import pandas as pd
import numpy as np
import re
import sqlite3
# from image_call imort image_pull

connect = sqlite3.connect('AllPrintings.sqlite')


# pipeline for optiyzation, 
def clean():
    df = pd.read_sql_query( 
    # will ned to pull name, rules text, cost, colosr, converted cost, type, types, 
    """SELECT * 
    FROM cards
    WHERE borderColor IS 'black' 
    """
    , connect)
    # make cleaning 
    df1 = deep_clean(df)
    return df1

def remove_redundant(redundant):
    name_, id_= [],[] # this code pulls unique names and id's of cards for removing reprints.
    for i,el in enumerate(redundant['name']):
        if el not in name_:
            name_.append(el)
            id_.append(redundant['scryfallId'][i])
    return redundant.query(f"scryfallId == {id_}")

def image_uri(dframe):# in need of change and imrpovement.
    list_ = []
    normal =[]
    json_pull = pd.read_json('json/scryfall-default-cards.json')
    for i in dframe['scryfallId']:
        list_.append(json_pull.query(f'id == "{i}"')['image_uris'].values[0])
    for i in list_:
        if type(i) == float:
            normal.append(False)
        else:
            normal.append(i['normal'])
    return normal

def deep_clean(frame_):
    frame_2 = frame_[['name', 'power', 'toughness', 'text',
     'types', 'type', 'subtypes', 'rarity', 'colorIdentity', 'colors',
      'convertedManaCost', 'manaCost', 'faceConvertedManaCost',  'side', 'scryfallId' ]]

    frame_3 = remove_redundant(frame_2)
    frame_4 = color_split(frame_3)
    is_commander = []
    for type1  in frame_4['type']:
        if type1.startswith('Legendary ') and 'Creature' in type1:
            is_commander.append(1)
        else: 
            is_commander.append(0)
    frame_4['is_commander'] = is_commander
    frame_4['uri'] = image_uri(frame_4)
    return frame_4

def color_split(color): # creates a get dummies for color cost and color identity, also drops new useless columns.
    names = ['Green','Blue','Black','Red','White']
    start_ = ['G','U','B','R','W']

    for i,el in enumerate(names): # creates columns with cost of colors and color identity
        # color cost VV
        color[f'manaCost_{el}'] = color['manaCost'].apply(lambda x: str(x).count(f'{start_[i]}'))
    # bellow gennerates cost of colorless. 
    color['manaCost_colorless'] = color['convertedManaCost'].astype('int') - sum(
        [color['manaCost_Green'],
        color['manaCost_Red'],
        color['manaCost_Black'],
        color['manaCost_Blue'], 
        color['manaCost_White']
        ])

    # color identity VV
    for i,el in enumerate(names):
        color[f'colorIdentity_{el}'] = color['colorIdentity'].apply(lambda x: str(x).count(f'{start_[i]}'))
    color['colorIdentity_colorless'] = [1 if x == True else 0 for x in color['colorIdentity'].isna()]
    # simplified for esier indexing.
    # temp = color[['colorIdentity_Black','colorIdentity_White','colorIdentity_Red','colorIdentity_Blue','colorIdentity_Green']]
    # color['color_identity'] = [temp.iloc[element].values.astype(int) for element in range(temp.shape[0])]
    color.drop(columns = ['manaCost','colors','colorIdentity'], inplace = True)
    return color

# try:
#     color = pd.read_csv('mtg_modern_clean.csv')
# except:
mtg_frame = clean()
mtg_frame.to_csv('mtg_modern_clean.csv')