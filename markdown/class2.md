## 🐍 今天學了什麼 Python 指令？

### 📏 1. `len()` 看字有幾個

```python
print(len("apple"))  # 結果是 5，因為 apple 有 5 個字母
print(len("."))  # 結果是 1，因為 . 是一個字元
```

👉 `len()` 是一個會告訴你一段文字有幾個字的「小幫手」。

---

### 🔍 2. `type()` 看是什麼種類

```python
type("Hello")  # 字串（文字）
type(123)      # 整數
type(1.23)     # 小數
```

👉 `type()` 是用來看一個東西是什麼種類（像是數字或文字）。

---

### 🔄 3. 型態轉換（把一種東西變成另一種）

```python
int(1.0)  # 小數變整數，結果是 1
float(1)  # 整數變小數，結果是 1.0
```

👉 常見的型態有：

- `int`：整數（像 1）
- `float`：小數（像 1.23）
- `str`：文字（像 "你好"）

---

### 🎤 4. `input()` 請使用者輸入資料

```python
a = input("請輸入你的名字：")
print("輸入結束")
print(type(a))  # 輸入的東西是字串（文字）
```

👉 `input()` 可以讓使用者輸入東西（例如：名字或數字）。

---

### 🧮 5. 計算圓的面積和直徑

```python
# 面積 = 3.14 x 半徑 x 半徑
radius = float(input("請輸入半徑："))
area = 3.14 * radius * radius
print(area)

# 直徑 = 半徑 x 2
diameter = 2 * radius
print(diameter)
```

👉 學會用變數來計算數學題。

---

### ✨ 6. Streamlit 是什麼？

Streamlit 是一個可以做「漂亮網頁」的小幫手。以下是常用的顯示方法：

```python
import streamlit as st

st.title("這是標題")  # 顯示大標題
st.write("這是一般文字")
st.text("這是純文字")
st.markdown("**粗體文字**")  # Markdown 語法
st.info("提示訊息")
st.success("成功訊息")
st.warning("警告訊息")
st.error("錯誤訊息")
```

👉 `st.write()` 是最常用的，幾乎什麼都能顯示！

---

### 🔢 7. `st.number_input()` 輸入數字

```python
number = st.number_input("請輸入一個數字：", step=1, min_value=0, max_value=100)
st.write(f"你輸入的數字是：{number}")
```

👉 可以讓使用者輸入數字（還可以設定最小值和最大值）。

---

### 🧪 8. 分數等級小幫手

```python
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
```

👉 這就是「成績評分機器」！輸入分數，它會告訴你等級。

---

### 🔐 9. 密碼門（如果...就...）

```python
password = input("請輸入密碼：")
if password == "1231":
    print("歡迎楚霖！")
else:
    print("密碼錯誤！")
```

👉 用 `if` 判斷對不對，對就歡迎，錯就說錯誤。

---

### ⚖️ 10. 比較運算子

```python
print(1 == 1)  # 一樣嗎？是 True
print(1 != 1)  # 不一樣嗎？False
print(1 > 1)   # 大於？False
print(1 >= 1)  # 大於或等於？True
```

👉 用來比較數字是不是一樣、哪個比較大。

---

### 🔗 11. 邏輯運算子（多條件判斷）

```python
print(True and True)   # 兩個都對 → True
print(True and False)  # 有一個錯 → False

print(not True)  # 變成 False
```

👉 `and` 是「而且」、`not` 是「不是」。

---

### 🧠 12. 順序很重要！(優先順序)

運算順序從高到低：

1. 括號 ()
2. 次方 \*\*
3. 乘 ÷
4. 加減 + -
5. 比較運算子（==, >, <）
6. not
7. and
8. or
