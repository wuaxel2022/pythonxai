"""
#這是多行註解
這邊可以放很多的文字
"""

# 這是單行註解
print("Hello World")  # print是在終端機顯示文字的指令
# ctrl+?可以快速註解 取消註解


# 基本型態
print(1)  # int這是整數, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
print(1.0)  # float這是浮點數
print(1.234)  # float這是浮點數
print("apple")  # str 這是字串 "sadasd123125557"， '1'
print(True)  # bool 這是布林值 True False
print(False)  # bool 這是布林值 True False

# 變數
a = 10  # 新增一個儲存空間並取名叫a "="的功能是將右邊的值10存入左邊的a
print(a)  # 終端機顯示a的值
a = "apple"  # 將a的值改為apple
print(a)  # 終端機顯示a的值

# 運算子
print(1 + 1)  # 加
print(1 - 1)  # 減
print(1 * 1)  # 乘
print(1 / 1)  # 除
print(1**1)  # 次方
print(1 % 1)  # 取餘數
print(1 // 1)  # 取商

# 優先順序
# 1. ()
# 2.**
# 3.乘 除 取商 取餘數
# 4. + - 加 減


# 字串運算 +' *
print("apple" + " pen ")  # 字串加
print("apple" * 3)  # 字串乘法

# 練習
a = "hello"
b = "world"
print(a + " " + b)

# 字串格式化
name = "apple"
age = 18
print(f"hello' my name is {name} and I am {age} years old")  #  f_string
# 變數 其他型態的資料放到f字串中的{} 可以在字串中顯示
