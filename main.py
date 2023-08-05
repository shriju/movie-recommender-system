import streamlit as st
import numpy as np
import pandas as pd

import pickle
import requests
import sklearn
from sklearn.metrics.pairwise import cosine_similarity

def fetch_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=93bc46ccddcebd303e5288dcca69c2d7'.format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path =  "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse =True, key = lambda x:x[1])

    recommended_movies_names = []
    recommended_movies_posters = []

    for i in distances[1:6]:
        # fetch movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_posters.append(fetch_poster(movie_id))

        recommended_movies_names.append(movies.iloc[i[0]].title)
    return recommended_movies_names, recommended_movies_posters


st.header('Movie Recommender System')
movies = pd.compat.pickle_compat.load(open('movies.pkl','rb'))
#df = pd.compat.pickle_compat.load('file.pkl')
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown",movie_list)



if st.button('Show Recommendation'):
    recommended_movies_names,recommended_movies_posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)


    with col1:
        st.text(recommended_movies_names[0])
        st.image(recommended_movies_posters[0])

    with col2:
        st.text(recommended_movies_names[1])
        st.image(recommended_movies_posters[1])
    with col3:
        st.text(recommended_movies_names[2])
        st.image(recommended_movies_posters[2])
    with col4:
        st.text(recommended_movies_names[3])
        st.image(recommended_movies_posters[3])
    with col5:
        st.text(recommended_movies_names[4])
        st.image(recommended_movies_posters[4])

