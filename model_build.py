import pandas as pd
import numpy as np
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

df = pd.read_csv('mtg_modern_clean.csv')
documents = df['text'].dropna()
vectorizer = TfidfVectorizer(stop_words='english')

X = vectorizer.fit_transform(documents)
true_k = 20
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)