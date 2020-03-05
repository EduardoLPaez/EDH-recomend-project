import streamlit as st
import pandas as pd
import numpy as np
from random import randint


data = pd.read_csv("mtg_modern_clean.csv")
test_img = 'https://img.scryfall.com/cards/normal/front/0/3/03f4341c-088b-4f35-b82b-3d98d8a93de4.jpg?1576382166'

selectbox = st.sidebar.selectbox(
    'Color explinations',('. . .','Blackck','White','Red','Blue','Green','Colorless')
    )
def roll_ ():
    st.write('extra to add fry. or later')

def select(choise):
    st.title(f'{choise}')
    if choise == 'Blackck':
        st.text('''
        Here is a short description of the functions of Blackck. for now its mostly
        just loremipsum type stuff.
        ''')
def top_commanders(in_): # filters commander collor identities
    data = data.query(f'is_commander == 1')
    uri = []
    if in_ == None: # filters colorless
        dta1 = data.query('colorIdentity_colorless == 1')
        uri = list(data[uri])
    else:# all others
        for i in in_:
            uri.append


def main(color_list = None, commander = None):
    if selectbox:
        select(selectbox)
    if color_list == None and commander == None:
        color_list = []
        st.title("EDH recommender")
        st.subheader('please pick a color or color combination for a commader.')
        st.markdown('''
            - hello, this aplication will require you to select the colors of the comander you are interested in.
            - click on one or more colors to add them to the list, then click next when you are done.
            - in the case you want to view colorless comanders then please click next with no colors selected.
            - in the case you donot know what color to pick please just select random.
        ''')
        if st.checkbox('Black'): # look for smalll img  for colors.
            if 'Black' in color_list:
                color_list.remove('Black')
            else:
                color_list.append('Black')
        if st.checkbox('White'):
            if 'White' in color_list:
                color_list.remove('White')
            else:
                color_list.append('White')
        if st.checkbox('Red'):
            if 'Red' in color_list:
                color_list.remove('Red')
            else:
                color_list.append('Red')
        if st.checkbox('Blue'):
            if 'Blue' in color_list:
                color_list.remove('Blue')
            else:
                color_list.append('Blue')
        if st.checkbox('Green'):
            if 'Green' in color_list:
                color_list.remove('Green')
            else:
                color_list.append('Green')

        if st.button('Next'):
            main(color_list)
        #if st.button('Random'):
            #command(roll_)   
    elif color_list != None and commander == None:
        st.title(f'Top Commanders for {color_list}')
        st.write('''
            - in order by most to least used.
        ''')
        uri = top_commanders(color_list)
        st.image(uri, width = None)

    elif color_list == None and commander != None:
        st.title(f'{commander}')
        st.image(recomend_(commander), width = None)
    
    else:
        main()
    

if __name__ == '__main__':
    main()
#st.write(data)
#st.image(test_img, width = None)


