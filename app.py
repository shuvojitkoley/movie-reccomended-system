import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url="https://api.themoviedb.org/3/movie/{}?api_key=ef6be52f4b3751b80ee01704b3e1abbe&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    recommended_movies_posters= []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        #fetch the poster
        recommended_movies.append(movies.iloc[i[0]].title)
        #fetch poster from api
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))
def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''

    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url("https://repository-images.githubusercontent.com/275336521/20d38e00-6634-11eb-9d1f-6a5232d0f84f");
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )

set_bg_hack_url()
st.write(
    f"""
    <div style="
        display: flex;
        justify-content: centre;
        align-items: centre;
        height: 10vh;
        background-color: transparent;
        color: #EAE163;
        font-size: 4rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px #000000;
        white-space: nowrap;
        text-align: centre;
        padding-right: 600px;
        ">
        Movie Recommender System
    </div>
    """,
    unsafe_allow_html=True
)
selected_movie_name = st.selectbox(
'How would you like to be contacted?',
movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)

    col1, col2,col3,col4,col5 = st.columns(5)
    with col1:
        name=names[0]
        modified_name = f"<span style='color:white'>{name}</span>"
        st.write(modified_name, unsafe_allow_html=True)
        st.image(posters[0])
    with col2:
        name=names[1]
        modified_name = f"<span style='color:white'>{name}</span>"
        st.write(modified_name, unsafe_allow_html=True)
        st.image(posters[1])
    with col3:
        name=names[2]
        modified_name = f"<span style='color:white'>{name}</span>"
        st.write(modified_name, unsafe_allow_html=True)
        st.image(posters[2])
    with col4:
        name=names[3]
        modified_name = f"<span style='color:white'>{name}</span>"
        st.write(modified_name, unsafe_allow_html=True)
        st.image(posters[3])
    with col5:
        name=names[4]
        modified_name = f"<span style='color:white'>{name}</span>"
        st.write(modified_name, unsafe_allow_html=True)
        st.image(posters[4])

    col6,col7,col8,col9,col10 = st.columns(5)
    with col6:
        name=names[5]
        modified_name = f"<span style='color:white'>{name}</span>"
        st.write(modified_name, unsafe_allow_html=True)
        st.image(posters[5])
    with col7:
        name=names[6]
        modified_name = f"<span style='color:white'>{name}</span>"
        st.write(modified_name, unsafe_allow_html=True)
        st.image(posters[6])
    with col8:
        name=names[7]
        modified_name = f"<span style='color:white'>{name}</span>"
        st.write(modified_name, unsafe_allow_html=True)
        st.image(posters[7])
    with col9:
        name=names[8]
        modified_name = f"<span style='color:white'>{name}</span>"
        st.write(modified_name, unsafe_allow_html=True)
        st.image(posters[8])
    with col10:
        name=names[9]
        modified_name = f"<span style='color:white'>{name}</span>"
        st.write(modified_name, unsafe_allow_html=True)
        st.image(posters[9])