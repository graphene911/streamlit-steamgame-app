import streamlit as st
from streamlit_player import st_player

def run_home() :
    st.title('')
    
    url = 'https://www.youtube.com/watch?v=82Y1azoaUhI'

    st_player(url)
    
    

    
    