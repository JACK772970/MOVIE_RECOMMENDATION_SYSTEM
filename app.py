import streamlit as st
import pickle
import pandas as pd

# Load saved files
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))


# Recommend function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    similarity_scores = similarity[movie_index]

    indexed_scores = list(enumerate(similarity_scores))
    sorted_movies = sorted(indexed_scores, reverse=True, key=lambda x: x[1])

    top_5 = sorted_movies[1:6]

    recommended = []
    for i in top_5:
        recommended.append(movies.iloc[i[0]].title)

    return recommended


# App UI
st.title("🎬 Movie Recommender System")
st.write("Select a movie and get 5 similar recommendations!")

# Dropdown of all movies
selected_movie = st.selectbox("Select a movie", movies['title'].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)

    st.write("Movies recommended for you:")
    for movie in recommendations:
        st.write("🎥", movie)