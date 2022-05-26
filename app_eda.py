import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns



def run_eda() :
    
    
    st.title('Game Info & EDA \n 스팀게임에서 제공하는 게임 정보와 평점과 가격, 다운로드수에 대한 EDA페이지 입니다.')

    
    df = pd.read_csv('data/steam.csv', index_col=0)

    st.info('본 데이터는 2022-05-20 기준 데이터입니다. Reference : https://www.kaggle.com/datasets/eringray/steam-games-dataset.')

    st.title('')
    
    st.subheader('Game Type별 인기순위 TOP10')
    
    game_type_list = ['Strategy', 'Action', 'RPG', 'Adventure', 'Indie', 'Simulation','Sports']

    my_choice = st.selectbox('Game Type 선택', game_type_list)

    if my_choice == game_type_list[0] :
        st.write('Stratgy 인기 TOP 10')
        st.dataframe(df.loc[df['Game_Type'] == 'Strategy'].head(10))
    elif my_choice == game_type_list[1] :
        st.write('Action 인기 TOP 10')
        st.dataframe(df.loc[df['Game_Type'] == 'Action'].head(10))
    elif my_choice == game_type_list[2] :
        st.write('RPG 인기 TOP 10')
        st.dataframe(df.loc[df['Game_Type'] == 'RPG'].head(10))
    elif my_choice == game_type_list[3] :
        st.write('Adventure 인기 TOP 10')
        st.dataframe(df.loc[df['Game_Type'] == 'Adventure'].head(10))
    elif my_choice == game_type_list[4] :
        st.write('Indie 인기 TOP 10')
        st.dataframe(df.loc[df['Game_Type'] == 'Indie'].head(10))
    elif my_choice == game_type_list[5] :
        st.write('Simulation 인기 TOP 10')
        st.dataframe(df.loc[df['Game_Type'] == 'Simulation'].head(10))
    elif my_choice == game_type_list[6] :
        st.write('Sports 인기 TOP 10')
        st.dataframe(df.loc[df['Game_Type'] == 'Sports'].head(10))

    st.title('')

    column_list = df.columns
    column_list = st.multiselect('스팀게임 데이터 카테고리별 보기 (중복 선택 가능)', column_list)

    if len(column_list) != 0 :
        st.dataframe(df[column_list])

    game_price_Owners_corr_df = df[['Game','Price','Download']].sort_values('Price', ascending=False)

    st.subheader('')
    if st.checkbox('가격, 다운로드 수, 평점의 상관관계 분석 차트보기') :
        col1, col2, col3 = st.columns(3)

        meta_down = Image.open('data\Metascore & Download Corr.png')
        col1.header("Metascore & Download Corr")
        col1.image(meta_down, use_column_width=True)
        
        price_down = Image.open('data\Price & Download Corr.png')
        col2.header("Price & Download Corr")
        col2.image(price_down, use_column_width=True)

        price_meta = Image.open('data\Metascore & Price Corr.png')
        col3.header("price & Metascore Corr")
        col3.image(price_meta, use_column_width=True)

    else :
        st.text('')
    
    pg_gm_df = pd.read_csv('data\pg_gm_df.csv')
    if st.checkbox('게임회사별 판매중인 게임의 갯수와 평균평점보기') :
        public_meta_mean_df = df.groupby('Publishers')['Metascore'].mean().to_frame()
        public_count_game_df = df.groupby('Publishers')['Game'].count().to_frame()
        public_meta_mean_df.columns = ['MetaScore_AVG']
        public_count_game_df.columns = ['Game_CNT']
        public_cnt_avg_df = public_count_game_df.join(public_meta_mean_df)
        public_cnt_avg_df = public_cnt_avg_df.sort_values('Game_CNT', ascending=False)
        st.dataframe(public_cnt_avg_df)
    else :
        st.text('')

    