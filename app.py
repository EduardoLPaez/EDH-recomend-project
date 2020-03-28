import streamlit as st
import pandas as pd
import numpy as np
from random import choice
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import joblib


data = pd.read_csv("mtg_modern_clean.csv")
card_model1 = joblib.load('models/language_kmeans.sav')

# pd.set_option('display.colwidth' , 500 )
# test_img = 'https://img.scryfall.com/cards/normal/front/0/3/03f4341c-088b-4f35-b82b-3d98d8a93de4.jpg?1576382166'
# _list = [0,0,0,0,0]


# def roll_(to ):
#     result = randint(2, 5)
#     return result
def cards(command, model = card_model1, df = data):# modify the size, also add recomendations, 
    command_text = list(data.query(f"name == '{command}'")['text'])[0]
    command_uri = list(data.query(f"name == '{command}'")['uri'])[0]
    st.image(command_uri)
    st.markdown(f'''
                - {command}:  
                - {command_text}
                ''')
    #cluster = model.predict(df.query(f'name == "{command}"')['text'])
    return #data.query(f'clusters == {cluster}')
def recomendations(commander_, set_ = data):
    cluster = set_['']
def print_card(comm, card = data ):
    st.subheader(card.query(f'name == "{comm}"')['name'])
    st.markdown(card.query(f'name == "{comm}"')['text']) # consider adding color identity in a redable format.
    
def color_correct(card_frame, comm, cframe = data):
    comm = cframe.query(f'name == "{comm}"')


    # frak.. 

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
    # lists used by select boxes in app.
    menu = ['start','explinations','color selection', 'card analysis']
    analisys_menu = ['start', 'types distribution']
    commanders = list(np.append(np.array(['chose']), data.query('is_commander == 1')['name'].sort_values()))

    # sidebar. need to learn how to make sidebar NOT a select box...
    choises = st.sidebar.selectbox('page', menu) # mor things to add
    
    if choises == 'start':
        st.title("EDH recommender")
        st.markdown('''
            - hello, this aplication will require you to select the colors of the comander you are interested in.
            - use the dropdown bar to the left to go to 'color select' to see commanders for certain color combinations. 
            - from there pick a commander name from the bar bellow that. and you will be recomended cards for it.
            - there is also a section for explanions on the colors and basic rules of commander also known as EDH(elder dragon hilander)
            as a format
        ''')
        #if st.button('Random'):
    if choises == 'explinations':
        st.title('color and format explibations')
        bar_choice = st.selectbox('section', ['color explination', 'EDH'])
        if bar_choice == 'EDH':# remember to pass writen text by text editor for spelling mistakes.. 
            st.title('EDH as a format')
            st.markdown('''
            the EDH format (also known as commander or Eldr Dragon Highlander), is an interesting format with simple rules.\n
            - first. all decks must have a commander
                - commanders must be legendary creatures.
                - some exeptions may apply. Said exeptions mention the clauses of their use in the card effects.
                - all commanders start the game in the command zone.
                - they can be cast from there whenever you could cast a creature. 
                - if the commander would change location (i.e. field to grave, grave to exile, field to deck, ect.) you may instead have it go to commander zone instead.
                - every time the commander is cast from the command zone after the first, the commander cost a cumulative 2 colorless more.(i.e. 2 after first, then 4,6 ,8, so on and soforth)
            - decks must be 100 cards. including the commander(s)
            - cards within the deck must be within the commander's color identity.
                - i.e. if the comander's color identity is Red Blue. all cards must have a color identity of
                    - Red, 
                    - Blue,
                    - Red + Blue
                    - colorless 
            - cards that generate colored mana can still generate mana of any color. but cannot have a color identity outside the commander's 
            - life totals start at 40.
            - there is no cap in the total number of players. 
            - if the number of partisipating players is greater than 2, all players draw 1 on their first turn.
            - most other rules are as normall in MTG.
            ''')   
        if bar_choice == 'color explination': # need to finish green
            st.title('color explination')
            st.subheader('Black')
            st.markdown('''
            Black is the color of power, death, and ambition. It uses any and all posible resources to gain the upperhand in a game.
            most cards in the color use the life total, hand, deck, or even other creatures on the field or off it as a resource to be
            expended for further advantage.\n when mixed with other colors, the result tends to be more specialized on using
            one resourece, genneraly black white focuses on using lifetotal, black blue abuses the hand and deck, black red focuses on creatures 
            and sacrefice, and black green focuses on recurring the graveyard at nauseum. 
            \nblack's weackness lies in its inability to deal with non creature permanents such as artifacts and enchanments. its goal tends to be to
            \nout value its opponents before the nonliving parts of the decks overwelm it.
            ''')
            st.subheader('White')
            st.markdown('''
            \nWhite is the color of healing, enchanment, and token armies. It specialises on fielding large numbers of smaller creatures and \naltering the rules of 
            engament to benefit them. It is filled with cards that heal the player, and keep creatires alive against all ods,\n or earradicate everithing for aclean 
            slate. when mixed into other colors white genneraly bolster some aspect of the color.\n white black focuses on modifiying the life total to your advantage,
            white blue has some of the strongest and most encompasing enchanments, white green can field massive armies of tokens, and white red
            is ussually associated with equipment artifacts. 
            \nwhite's weackness lies in its speed. Its deffencive nature has a tendency to slow it down though its versatily and ability to whipe the board clean
            if nessesary compensate for it. 
            ''')
            st.subheader('Red')
            st.markdown("""
            Red is the color of emotion, destruction, and freedom. it hits the board fast, and its enemies faster. \nas a color it has the largest asortment of
            damaging options of any color, rainging from creatures to fire and lightning spelles, to creature effects, \nand a pile of artifacts and artifact supporrt
            for good measure. when mixed with other colors it tends to add a good degree of speed without messing with the other color most the time.
            \nblack red focus on sacrefising smaller creatures to burn away ate the enemy, white red on building armies and equiping them with artifacts to\n burn away at their enemies,
            red green on rushing green's ussual colosi to board even earlier to burn away their enemies,\n and red blue on the largest most conveluded conflagration imaginable.
            to burn away their enemies....
            \nOver all red is weack to its own speed. if an enemy is not dead when red runs out of steam,\n then there is little red can do.
            """)
            st.subheader('Blue')
            st.markdown('''
            Blue is the color of knolege, curiosity, and magic. it is the slowest color of the five, but makes up for it with a slew of
            spells and creature effects to slow the pace of the game to its liking. it is the only color with reliable counter spells, to the 
            chagrin of most other players on the table. it brings a great amount of controll to most colors it mixes with.
            \n Blue Black is all about removing options for your enemies by attacking their deck and hand. Blue White 
            dictates the pace of the game with slews of enchanments and swarms of flying creatures. Blue Red fight more like clasical 
            wizards, lightning bolts, fireballs, and all maner of lar scale spells. Blue Green, may quite well be the slowest 
            color combination of the duo colors, yet wields the largest amount of raw resources for
            both grenns usual colosi and blues own variation on such.
            \n over all Blue's weackness is its lack of direct offencive. While it exels at messing with their enemies flow
            it lacks a viable offencive till later into a game. 
                    ''')
            st.subheader('Green')
            st.markdown(''' 
            Green is the color of nature, life, growth. While it usually fields few creatures, these few tend to be 
            quite large. ussually this would make the color unbelibably slow, howerver coupeled with its nearly complete
            monopoly in spells focused on adding more resources to the board, they tend to show up earlier than some would
            think.
            \n when combined wih other colors green ussually brings its ability to ramp up to the other colors. 
            Green Black abuse Black's ability to revive and greens resources to create a trully resilient undying army.
            Green White brings Green's fuel to White's token armies, trully blowing their scales out of proporsion.
            Green Red mix the trully scarry size of Green, and Red's speed of deployment leading to what is likely 
            the most agressive of the color combinations. 
            Green Blue, use Blue's controll and Green's resources and size to qute litteraly   
            ''')                
    if choises == 'color selection':# need to add check for vaiable plainwalker commanders
        commander = st.selectbox('commanders', commanders)
        if commander == 'chose':
            st.title('Commander colors')
            st.markdown('''- all decks in the EDH format have a comander. the commanders color \nidentity determines what cardscan be added to it
                        - an exploration of which is in the color explination section.
                        - please select a color from the check list bellow.
                        - you can then find the information on the comander in the scroll down to the left 
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
        if commander != 'chose':
            st.title(f'{commander}')
            cards(commander)
            # recomendations(commander)
            # cards = color_correct(cards, commander).reset_index()

            # for i in range(30):
            #     print_cards(cards.loc[i])
    if choises == 'card analysis': # see if we can predict cmc....
        st.title('Genral analysis')
        analysis_choice = st.selectbox('section', analisys_menu)
        if analysis_choice == 'start':
            st.subheader('Hello')
            st.markdown('this section is for the analisys\n and exploration of the mtg data\n select a section from the bar above.\n and have fun. :D\n')
        if analysis_choice == 'types distribution':
            st.subheader('working on it')
    
        

if __name__ == '__main__':
    main()