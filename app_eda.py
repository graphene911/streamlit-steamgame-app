import streamlit as st


def run_eda() :
    st.subheader('평점과, 가격, 다운로드수에 대한 상관관계 분석 페이지 입니다.')

    df = pd.read_csv('data/steam.csv')

    st.dataframe(df)