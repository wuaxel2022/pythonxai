import streamlit as st

# st.number_input()可以讓使用者輸入數字
# step=1可以讓使用者輸入整數
# min_value=0可以讓使用者輸入不小於0的數字
# max_value=100可以讓使用者輸入不大於100的數字
number = st.number_input("請輸入一個數字：", step=1, min_value=0, max_value=100)
# 顯示使用者的數字
st.write(f"你輸入的數字是：{number}")

st.write("---")

st.write("## 練習")
score = st.number_input("請輸入你的分數", min_value=0, max_value=100, step=1)
if score >= 90:
    st.write("你的等級是A")
elif score >= 80:
    st.write("你的等級是B")
elif score >= 70:
    st.write("你的等級是C")
elif score >= 60:
    st.write("你的等級是D")
else:
    st.write("你的等級是F")
