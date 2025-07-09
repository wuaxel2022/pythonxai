import streamlit as st

# st.write("### 按鈕練習")
# st.button()可以在畫面上顯示按鈕 使用者可以點擊按鈕
# key是按鈕的名稱
# 如果使用者點擊按鈕  st.button()就會回傳True
st.button("按我一下", key="btn1")
if st.button("按我一下", key="btn2"):
    st.balloons()
if st.button("按我一下", key="btn3"):
    st.snow()
st.write("---")

st.write("### 數字練習")
num = st.number_input("請輸入一個整數(1到9)", min_value=1, max_value=9, step=1)
for i in range(1, num + 1):
    st.write(f"{i}" * i)
