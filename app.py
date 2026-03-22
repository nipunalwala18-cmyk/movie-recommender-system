import streamlit as st
import pickle
import requests
import pandas as pd

movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

def fetch_poster_by_title(title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key=8952660ddf2e2a1993f34f1af9eefb79&query={title}"
    
    data = requests.get(url).json()
    
    if data['results']:
        poster_path = data['results'][0]['poster_path']
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)), 
                         reverse=True, 
                         key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []

    for i in movies_list:
        title = movies.iloc[i[0]].title
        recommended_movies.append(title)
        recommended_movies_poster.append(fetch_poster_by_title(title))

    return recommended_movies, recommended_movies_poster


st.title("Movie Recommendation System")

selected_movie_name = st.selectbox('Select Movies: ', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3 = st.columns(3)

    # First row (3 movies)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    # Second row (remaining 2 movies)
    col4, col5 = st.columns(2)

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])