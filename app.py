import streamlit as st
import pandas as pd
from PIL import Image
from app_eda import run_eda

from app_home import run_home
from streamlit_player import st_player

def main() :
    pass

st.set_page_config(layout="wide")



img1 = Image.open('data\steam_logo2.jpg')
st.image(img, width=1035)
st.subheader('')
st.info('이 앱은 스팀게임의 평점 및 가격데이터를 확인하는 앱 입니다.')
st.title('')


menu = ['Home', 'Game Info']
img2 = Image.open('data\steam_logo1.jpg')
st.sidebar.image(img, width=305)

    

df = pd.read_csv('data/steam.csv', index_col=0)
game_serch = st.sidebar.text_input('게임 검색')
result = df.loc[ df['Game'].str.lower().str.contains(game_serch.lower()),]

if st.button('게임검색 확인') :
    st.dataframe(result)
else :
    st.text('')

choice = st.sidebar.selectbox('메뉴 선택', menu)


if choice == menu[0] :
    run_home()
elif choice == menu[1] :
    run_eda()








if __name__ == '__main__' :
    main()