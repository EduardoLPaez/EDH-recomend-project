import streamlit as st
import pandas as pd
import numpy as np
from random import randint


data = pd.read_csv("mtg_modern_clean.csv")
# pd.set_option('display.colwidth' , 500 )
# test_img = 'https://img.scryfall.com/cards/normal/front/0/3/03f4341c-088b-4f35-b82b-3d98d8a93de4.jpg?1576382166'
# _list = [0,0,0,0,0]


def roll_():
    result = randint(2, 5)
    return result

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

def top_commanders(in_, frame = data): # filters commander collor identities
    colors =  ['Black','White','Red','Blue','Green']
    frame = frame.query('is_commander == 1')
    if in_ == [False,False,False,False,False]:
        color = ['colorless']
    else:
        color = [b for a, b in zip(in_, colors) if a]
        if in_ != [True, True, True, True, True]:
            not_color = [b for a, b in zip(in_, colors) if not a]
            for i in not_color:
                frame = frame.query(f'colorIdentity_{i} != 1')
    for i in color:
        frame = frame.query(f'colorIdentity_{i} == 1')
    
    return frame['name'],list(frame['text'])# list(frame.query('uri != "0"').dropna()['uri'])#.sortvalues(by =['use'], ascending = False) # as above


def main():
    
    menu = ['start','color explination','color selection']
    choises = st.sidebar.selectbox('page', menu)
    if choises == 'start':
        st.title("EDH recommender")
        st.markdown('''
            - hello, this aplication will require you to select the colors of the comander you are interested in.
            - use the dropdown bar to the left to select weather you would like to look at mono, dual,
            tri, quad, chomatic, or colorless comanders. 
            - from there select a comander name and you will get card recomendations for it.
            - there is also a section for explaning the colors and basic rules of commander also known as EDH(elder dragon hilander)
            as a format
            - or you could just look for a random commander by cliking bellow.
        ''')
        if st.button('Random'):
            st.write('move to random cmmander name')
            
    if choises == 'color selection':
        st.title('Commander colors')
        st.markdown('''- all decks in the EDH format have a comander. the commanders color identity determines what cards
                    can be added to it
                    - an exploration of which is in the color explination section.
                    - please select a color from the check list bellow then click next. 
                ''')
        cb1 = st.checkbox('Black',)
        cb2 = st.checkbox('White')
        cb3 = st.checkbox('Red')
        cb4 = st.checkbox('Blue')
        cb5 = st.checkbox('Green')
        uri_return = top_commanders([cb1,cb2,cb3,cb4,cb5])
        for i,el in enumerate(uri_return[0]):
            st.markdown(f'''
            - {el}:  
            - {uri_return[1][i]}
            ''')
    

if __name__ == '__main__':
    main()
#st.write(data)
#st.image(test_img, width = None)


