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
    if choise == 'Black':
        st.text('''
        Black is the color of power, death, and ambition. It uses any and all posible resources to gain the upperhand in a game.
        most cards in the color use the life total, hand, deck, or even other creatures on the field or off it as a resource to be
        expended for further advantage. when mixed with other colors, the result tends to be more specialized on using
        one resourece, genneraly black white focuses on using lifetotal, black blue abuses the hand and deck, black red focuses on creatures 
        and sacrefice, and black green focuses on recurring the graveyard at nauseum. 
        black's weackness lies in its inability to deal with non creature permanents such as artifacts and enchanments. its goal tends to be to
        out value its opponents before the nonliving parts of the decks overwelm it.
        ''')
    elif choise == 'white':
        st.text('''
        White is the color of healing, enchanment, and token armies. It specialises on fielding large numbers of smaller creatures and altering the rules of 
        engament to benefit them. It is filled with cards that heal the player, and keep creatires alive against all ods, or earradicate everithing for aclean 
        slate. when mixed into other colors white genneraly bolster some aspect of the color. white black focuses on modifiying the life total to your advantage,
        white blue has some of the strongest and most encompasing enchanments, white green can field massive armies of tokens, and white red
        is ussually associated with equipment artifacts. 
        white's weackness lies in its speed. Its deffencive nature has a tendency to slow it down though its versatily and ability to whipe the board clean
        if nessesary compensate for it. 
        ''')
    elif choise == 'Red':
        st.text("""
        Red is the color of emotion, destruction, and freedom. it hits the board fast, and its enemies faster. as a color it has the largest asortment of
        damaging options of any color, rainging from creatures to fire and lightning spelles, to creature effects, and a pile of artifacts and artifact supporrt
        for good measure. when mixed with other colors it tends to add a good degree of speed without messing with the other color most the time. 
        black red focus on sacrefising smaller creatures to burn away ate the enemy, white red on building armies and equiping them with artifacts to burn away at their enemies,
        red green on rushing green's ussual colosi to board even earlier to burn away their enemies, and red blue on the largest most conveluded conflagration imaginable.
        to burn away their enemies....
        over all red is weack to its own speed. if an enemy is not dead when red runs out of steam, then theere is little red can do.
        """)

def top_commanders(in_): # filters commander collor identities
    data = data.query(f'is_commander == 1')
    uri = []
    if in_ == None: # filters colorless
        dta1 = data.query('colorIdentity_colorless == 1')
        uri = list(data[uri])
    else: # all others
        for i in in_:
            temp = data[f'colorIdentity_{in_}','name','uri','use']
            uri.append((temp['uri'], temp['use']))# need to set a condicional for this. somehow..
        uri_df = pd.DataFrame(data = uri, columns = ['uri', 'use'])
    return uri.uniques.sortvalues(by =['use'], ascending = False)


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


