import streamlit as st
from streamlit_player import st_player

def run_home() :
    
    st.subheader('이 앱은 스팀게임의 평점 및 가격데이터를 확인하는 앱 입니다.')
    st.info('좌측 사이드바의 메뉴 선택을 통해 데이터를 확인 할 수 있습니다.')

    url = 'https://www.youtube.com/watch?v=82Y1azoaUhI'

    st_player(url)
    