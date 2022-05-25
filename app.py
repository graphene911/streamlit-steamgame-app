from asyncio import run_coroutine_threadsafe
import streamlit as st
import pandas as pd
from PIL import Image
from app_eda import run_eda

from app_home import run_home




def main() :
    pass

st.title('Steam Games Exploratory Data Analysis App')
menu = ['Home', 'EDA', 'GAME INFO']
img = Image.open('data\steam_logo1.jpg')
st.sidebar.image(img, width=305)
choice = st.sidebar.selectbox('메뉴 선택', menu)


if choice == menu[0] :
    run_home()
elif choice == menu[1] :
    run_eda()
elif choice == menu[2] :
    pass

df = pd.read_csv('data/steam.csv', index_col=0)
game_serch = st.sidebar.text_input('게임 검색')
result = df.loc[ df['Game'].str.lower().str.contains(game_serch.lower()),]
st.dataframe(result)





if __name__ == '__main__' :
    main()