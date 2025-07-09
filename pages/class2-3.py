# 比較運算子
print(1 == 1)  # true
print(1 != 1)  # false
print(1 > 1)  # false
print(1 < 1)  # false
print(1 >= 1)  # true
print(1 <= 1)  # true

# # 邏輯運算子

print(True and True)  # true
print(True and False)  # false
print(False and True)  # false
print(False and False)  # false

# not 運算子
print(not True)  # false
print(not False)  # true

# 優先順序
# 1. () 括號
# 2.** 次方
# 3.乘 除 取商 取餘數
# 4.+ - 加 減
# 5.比較運算子
# 6. not
# 7. and
# 8. or


# 密碼門檢查
password = input("請輸入密碼：")
if password == "1234":
    print("歡迎楚霖！")
elif password == "4567":
    print("歡迎楚霖的媽媽！")
elif password == "7890":
    print("歡迎楚霖的爸爸！")
else:  # 否則
    print("密碼錯誤！")
