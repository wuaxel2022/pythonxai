print(len("apple"))  # len()是一個函數，可以幫我們知道一個字串的長度
print(len("."))  # len()是一個函數，可以幫我們知道一個字串的長度
# type()  #可以查看一個變數的型態

# 型態轉換
print(int(1.0))  # float轉int
print(int(1))  # int轉float
print(float(1))  # int轉str
print(float(1))  # int轉boal
print(int(1.0))  # float轉int
print(int(1.234))  # float轉int
print(float(1.234))  # str轉float

# input()函式的使用
a = input("請輸入你的名字：")
print("輸入結束")
print(int(a) + 10)
print(type(a))  # 證明透過input()函式取得的是字串

# 計算圓的面積
radius = float(input("請輸入半徑："))
area = 3.14 * radius * radius
print(area)


# 計算圓的半徑
radius = float(input("請輸入半徑："))
diameter = 2 * radius
print(diameter)
