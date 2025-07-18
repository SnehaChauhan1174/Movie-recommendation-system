import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(title):
    response=requests.get(f'https://www.omdbapi.com/?t={title}&apikey=22df2e8e')
    data=response.json()
    return data['Poster']

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(mov):
    movie_idx = movies[movies['title'] == mov].index[0]
    dist = similarity[movie_idx]
    movies_list = sorted(list(enumerate(dist)),reverse=True, key=lambda x:x[1])[1:6]

    recommended=[]
    mov_ids=[]
    recomm_poster=[]
    for i in movies_list:
        mov_id=i[0]
        #fetch the movies images using api
        mov_ids.append(i[0])
        recommended.append(movies.iloc[i[0]].title)
        recomm_poster.append(fetch_poster(movies.iloc[i[0]].title))
    return recommended,mov_ids,recomm_poster

st.title("Movie Recommedation System")

option = st.selectbox(
    'For which movie do you want recommendation?',
    movies['title'].values
)
def get_omdb_poster(title,API_KEY):
    url=f"https://www.omdbapi.com/?t={title}&apikey={API_KEY}"
    res=requests.get(url).json()
    return res.get("Poster")


if st.button('Get Movie Recommendation'):
    recommendation,movie_ids,posters=recommend(option)
    for title in recommendation:
        poster_url=get_omdb_poster(title,"22df2e8e")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:

        st.markdown(f"<h5 style='text-align: center'>{recommendation[0]}</h5>", unsafe_allow_html=True)

        st.image(posters[0])
    with col2:
        st.markdown(f"<h5 style='text-align: center'>{recommendation[1]}</h5>", unsafe_allow_html=True)
        st.image(posters[1])
    with col3:
        st.markdown(f"<h5 style='text-align: center'>{recommendation[2]}</h5>", unsafe_allow_html=True)
        st.image(posters[2])
    with col4:
        st.markdown(f"<h5 style='text-align: center'>{recommendation[3]}</h5>", unsafe_allow_html=True)
        st.image(posters[3])
    with col5:
        st.markdown(f"<h5 style='text-align: center'>{recommendation[4]}</h5>", unsafe_allow_html=True)
        st.image(posters[4])


