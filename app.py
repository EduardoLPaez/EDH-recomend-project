import streamlit as st
import pandas as pd
import numpy as np

st.title("EDH recommender")
data = pd.read_csv("mtg_whole_clean.csv")

# @st.cache
# def load_data(nrows):

st.subheader('Raw data')
st.write(data)