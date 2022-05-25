import streamlit as st
import pandas as pd
from PIL import Image




def run_eda() :
    st.subheader('스팀게임의 평점과, 가격, 다운로드수에 대한 상관관계 분석 페이지 입니다.')

    img = Image.open('data\steam_logo2.png')
    st.image(img, width=850)
    df = pd.read_csv('data/steam.csv', index_col=0)

    st.info('본 데이터는 2022-05-20 기준 데이터입니다. Reference : https://www.kaggle.com/datasets/eringray/steam-games-dataset.')

    
    if st.button('전체 데이터 보기') :
        st.dataframe(df)

    column_list = df.columns
    column_list = st.multiselect('스팀게임 데이터 선택 보기', column_list)

    if len(column_list) != 0 :
        st.dataframe(df[column_list])

    
    