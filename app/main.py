import pickle
import streamlit as st
import pandas as pd

# Load anime data
animes = pickle.load(open('anime_list.pkl', 'rb'))
anime_names = animes["Name"].values()
animes = pd.DataFrame(animes)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Anime Recommender System')
st.write("Welcome! This recommender system suggests anime similar to the one you choose, helping you discover new shows you might enjoy.")

# User selects an anime
anime_selected = st.selectbox("Type or select an anime:", anime_names)

# Display recommended anime when button is clicked
if st.button('Show Recommendations'):
    idx = animes[animes["Name"] == anime_selected].index[0]
    similarities = similarity[idx]
    sorted_indices = similarities.argsort()[::-1][1:6]
    recommended_animes = animes.iloc[sorted_indices]["Name"].values

    st.subheader('Recommended Anime')
    if recommended_animes.size > 0:
        cnt = 1
        for anime in recommended_animes:
            st.write(str(cnt)+". "+anime)
            cnt+=1
    else:
        st.write("No recommendations found.")

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;

text-align: center;
}
</style>
<div class="footer">
<p>Made with ❤ by <a href="https://github.com/atharv-patil" target="_blank"> Atharv</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)