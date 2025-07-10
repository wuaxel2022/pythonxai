---
# 🐍 今天的 Python 小筆記

## 🖼️ 我們用 Streamlit 來做互動的畫面！

### 一、`欄位` 是什麼？

欄位就像把網頁分成幾個直的區塊，可以在每一個區塊放東西。

```python
col1, col2 = st.columns(2)
```

這行意思是：我把畫面分成兩欄。然後我可以在每欄放按鈕或文字。

```python
col1.button("按鈕1")
col2.button("按鈕2")
```

我們也可以用比例來控制每一欄多寬：

```python
col1, col2 = st.columns([1, 2])
```

這樣代表：col2 是 col1 的兩倍寬！

還可以放 3 欄、4 欄甚至更多：

```python
cols = st.columns(4)
```

用 `for` 迴圈還可以自動幫每一欄加東西。
---

### 二、`文字輸入` 的方式

```python
text = st.text_input("請輸入文字", value="這是預設文字")
st.write(f"你輸入的文字是:{text}")
```

上面是讓使用者輸入一些文字，然後顯示出來！

---

### 三、記住資料的 `session_state`

程式有時候會記不住資料（像是變數會重新開始），我們可以用 `session_state` 來幫助記憶。

```python
if "ans1" not in st.session_state:
    st.session_state.ans1 = 1

if st.button("按下去ans1加1"):
    st.session_state.ans1 += 1

st.write(f"ans={st.session_state.ans1}")
```

這樣不管按幾次按鈕，它都會記得目前是多少！

---

### 四、做一個簡單的點餐機！

#### 輸入食物名稱 → 加入購物籃：

```python
foolInput = st.text_input("請輸入餐點")
if st.button("加入"):
    st.session_state.order.append(foolInput)
```

#### 顯示餐點清單並可以刪除：

```python
for i in range(len(st.session_state.order)):
    st.write(st.session_state.order[i])
    if st.button("刪除", key=i):
        st.session_state.order.pop(i)
        st.rerun()  # 重新整理畫面
```

---

## 🧮 算數運算子小教室

這些是一些常見的加減乘除方式：

```python
a = 1
a += 1  # 加1
a -= 1  # 減1
a *= 2  # 乘2
a /= 2  # 除2
a %= 2  # 取餘數
a **= 2  # 平方
```

---

## ✨ 算式的優先順序（誰先算？）

1. 括號 `()`
2. 次方 `**`
3. 乘除 `* /`
4. 加減 `+ -`
5. 比大小 `== > <`
6. 邏輯 `and or not`
7. 其他特殊運算

---

## 🔁 迴圈 while、for 是什麼？

### while 會一直做，直到不符合條件：

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

也可以加 `for` 裡面再跑一次：

```python
i = 0
while i < 5:
    print(i)
    for j in range(5):
        print(j)
    if i == 3:
        break
    i += 1
```

---

## 🎲 random 隨機產生數字！

```python
import random

print(random.randint(1, 6))  # 隨機1~6（像骰子）
```

---

## 🧺 字典 dict：一種可以記住東西的資料格式

像這樣的字典：

```python
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
```

我們可以：

- 找出數字：`d["蘋果"]`
- 修改數字：`d["蘋果"] = 10`
- 加入水果：`d["蓮霧"] = 15`
- 刪除水果：`d.pop("蘋果")`
- 列出所有水果和價格：

```python
for k, v in d.items():
    print(f"{k}: {v}")
```

---

## 🎉 今天學了好多東西：

- 如何把畫面分成不同欄位
- 如何讓使用者輸入文字或按按鈕
- 學會了記住資料的方法（session_state）
- 用 `while` 和 `for` 做重複動作
- 使用 `random` 來做點遊戲
- 學會了用字典記錄資料（像是水果的價格）

---
