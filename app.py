import streamlit as st




def main() :
    pass

st.title('Steam Games의 별점 및 가격을 확인할 수 있는 앱')

menu = ['Home', 'EDA', 'GAME SELECT']

choice = st.sidebar.selectbox('메뉴 선택', menu)

if choice == menu[0] :
    run_home()
elif choice == menu[1] :
    run_eda()
elif choice == menu[2] :
    pass




if __name__ == '__main__' :
    main()