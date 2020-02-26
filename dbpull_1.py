import pandas as pd
import sqlite3
# connection: 
connect = sqlite3.connect('AllPrintings.sqlite')

# total of 50412 cards in the db,]
# about 18,006 are black border as of guilds of ravnica NEED TO ACCOUNT FOR. ie normally playable
# for some reason it returns 43,445 total black bordered cards...
# there are 20144 total unique names in it. . . 442 for each basic land, 
# seems that each unique print of them is counted. 
# will need to  

mtg_data = pd.read_sql_query( 
    # will ned to pull name, rules text, cost, colosr, converted cost, type, types, 
    """SELECT * 
    FROM cards
    WHERE borderColor IS 'black' 
    """
    ,
    connect
)
mtg_data.to_csv("mtg_modern_whole.csv")