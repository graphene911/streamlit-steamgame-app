import streamlit as st
import pandas as pd
from PIL import Image
from app_eda import run_eda
from app_home import run_home
from streamlit_player import st_player

import matplotlib.pyplot as plt
import seaborn as sb
def main() :
    

    st.set_page_config(layout="wide")



    img1 = Image.open('data/steam_logo2.jpg')
    st.image(img1, width=1035)
    st.subheader('')
    st.title('Game Info & EDA \n 스팀게임에서 제공하는 게임 정보와 평점과 가격, 다운로드수에 대한 EDA페이지 입니다.')
    
    st.title('')

    url = 'https://www.youtube.com/watch?v=82Y1azoaUhI'

    st_player(url)

    
    img2 = Image.open('data/steam_logo1.jpg')
    st.sidebar.image(img2, width=305)

    st.subheader('검색하신 게임을 확인하세요.')
    
    df = pd.read_csv('data/steam.csv', index_col=0)
    
    game_serch = st.sidebar.text_input('게임 검색')
    result = df.loc[ df['Game'].str.lower().str.contains(game_serch.lower()),]

    st.dataframe(result)
    st.text('본 데이터는 2022-05-20 기준 데이터입니다. \nReference : https://www.kaggle.com/datasets/eringray/steam-games-dataset.')
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

    

    st.subheader('')
    st.title('')
    st.text('Metascore가 가장 높은 게임입니다.')
    st.dataframe(df.loc[df['Metascore'] == df['Metascore'].max()])
    st.text('Metascore가 가장 낮은 게임입니다. ')
    st.dataframe(df.loc[df['Metascore'] == df['Metascore'].min()])
    st.subheader('')
    

    
    if st.checkbox('가격, 다운로드 수의 상관관계 및 분석 차트보기') :
               
        game_price_down_corr_df = df[['Game','Price','Download']].sort_values('Price', ascending=False)
        fig1 = plt.figure()
        
        sb.regplot(data=game_price_down_corr_df, x='Price', y='Download')
        plt.title('Price & Download Corr')
        plt.xlabel('Price')
        plt.ylabel('Download')
        plt.show()
                
        st.pyplot(fig1)
        st.dataframe(game_price_down_corr_df.corr())
    else :
        st.text('')

    if st.checkbox('평점, 다운로드 수의 상관관계 분석 및 차트보기') :
               
        game_meta_down_corr_df = df[['Game','Metascore','Download']].sort_values('Metascore', ascending=False)
        fig2 = plt.figure()
        
        sb.regplot(data=game_meta_down_corr_df, x='Metascore', y='Download')
        plt.title('Metascore & Download Corr')
        plt.xlabel('Metascore')
        plt.ylabel('Download')
        plt.show()
                
        st.pyplot(fig2)
        st.dataframe(game_meta_down_corr_df.corr())
    else :
        st.text('')

    if st.checkbox('가격과 평점의 상관관계 분석 및 차트보기') :
               
        game_meta_price_corr_df = df[['Game','Metascore','Price']].sort_values('Price', ascending=False)
        fig3 = plt.figure()
        
        sb.regplot(data=game_meta_price_corr_df, x='Metascore', y='Price')
        plt.title('Metascore & Price Corr')
        plt.xlabel('Metascore')
        plt.ylabel('Price')
        plt.show()
                
        st.pyplot(fig3)
        st.dataframe(game_meta_price_corr_df.corr())
    else :
        st.text('')
    
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
    








if __name__ == '__main__' :
    main()