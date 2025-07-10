import streamlit as st

st.title("欄位元件")
col1, col2 = st.columns(2)  # 2columns
col1.button("按鈕1", key="button1")
col2.button("按鈕2", key="button2")

# 2columns, 可以用比例來設定每個column的寬度
col1, col2 = st.columns([1, 2])
col1.button("按鈕3", key="btn3")
col2.button("按鈕4", key="btn4")

# 3columns
col1, col2, col3 = st.columns([1, 2, 3])
col1.button("按鈕5", key="btn5")
col2.button("按鈕6", key="btn6")
col3.button("按鈕7", key="btn7")

col1, col2 = st.columns([1, 2])
with col1:  # 在col1中建立一個按鈕
    st.write("這是col1")
    if st.button("按鈕8", key="btn8"):
        st.balloons()
with col2:
    st.write("這是col2")
    st.button("按鈕9", key="btn9")

# 多個columns
cols = st.columns(4)
for i in range(len(cols)):
    with cols[i]:
        st.button(f"for當中的按鈕{i+1}", key=f"多col{i+10}")

st.write("---")
st.write("columns排列元件效果比較")

col1, col2 = st.columns(2)
with col1:
    st.write("按鈕1", key="btn10")
    st.write("按鈕2", key="btn11")
    st.write("按鈕3", key="btn12")
with col2:
    st.write("這是col2")
    st.write("這是col2")
    st.write("這是col2")
st.write("---")

for i in range(3):
    col1, col2 = st.columns(2)
    with col1:
        st.button(f"按鈕{i+1}", key=f"排版測試{i+4}")
    with col2:
        st.write(f"這是col2_{i+1}")

st.write("---")
st.write(" 文字輸入元件")
text = st.text_input("請輸入文字", value="這是預設文字")
st.write(f"你輸入的文字是:{text}")


st.title("session_state")
ans = 1  # 設定一個變數ans = 1
if st.button("按下去ans加1", key="ans"):
    ans = ans + 1
st.write(f"ans的值是:{ans}")

# session_state
if "ans1" not in st.session_state:  # 如果session_state中沒有ans這個變數
    st.session_state.ans1 = 1  #

if st.button("按下去ans1加1", key="ans2"):
    st.session_state.ans1 = st.session_state.ans1 + 1
st.write(f"ans={st.session_state.ans1}")

if st.button("重新整理畫面", key="banana"):
    st.rerun()
