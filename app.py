import streamlit as st
import pandas as pd
import numpy as np

st.title("EDH recommender")
data = pd.read_csv("mtg_modern_clean.csv")
#pd.read_csv('images/img_clean.csv')

# @st.cache
# def load_data(nrows):

st.subheader('image test')
#st.write(data)
st.image('https://img.scryfall.com/cards/normal/front/0/3/03f4341c-088b-4f35-b82b-3d98d8a93de4.jpg?1576382166', width = None)


# 03f4341c-088b-4f35-b82b-3d98d8a93de4
# 03f4341c-088b-4f35-b82b-3d98d8a93de4
# 4dd3219b-2923-425d-9dc8-c346a89d7d66