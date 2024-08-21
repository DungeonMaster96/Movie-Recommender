import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_title):    
    try:
        # Use the OMDb API to fetch the movie poster by IMDb ID
        response = requests.get(f'http://www.omdbapi.com/?t={movie_title}&apikey=7327009b')
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        
        # Check if the poster is available
        if 'Poster' in data and data['Poster'] != "N/A":
            return data['Poster']
        else:
            return None  # Return None if no poster is available
    
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")
        return None
    except ValueError:  # Includes JSONDecodeError
        st.error("Error decoding JSON response")
        return None

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_posters = []
    
    for i in movies_list:
        movie_title = movies.iloc[i[0]].title
        recommended_movies.append(movie_title)
        
        # Fetch poster from OMDb API
        poster = fetch_poster(movie_title)
        recommended_movies_posters.append(poster)
        
    return recommended_movies, recommended_movies_posters

# Load data
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Streamlit UI
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Select a movie:",
    movies['title'].values
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)
    
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.write(f"<div style='text-align: center; word-wrap: break-word;'>{names[idx]}</div>", unsafe_allow_html=True)

            if posters[idx]:  # Only display image if poster URL is not None
                st.image(posters[idx], use_column_width=True)
            else:
                st.text("No poster available")
