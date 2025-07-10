# 算數指定運算子
a = 1
a += 1
print(a)
a -= 1
print(a)
a *= 2
print(a)
a /= 2
print(a)
a %= 2
print(a)
a **= 2
print(a)


# 優先順序
# 1. 括號 ()
# 2. 指數 **
# 3. 乘除 * /
# 4. 加減 + -
# 5. 比較評估 == != > < >= <=
# 6. 邏輯運算子 and or not
# 7. 位元運算子 & | ^
# 8. 取位 << >>
# 9. 位元運算子 ~
# 10. 其他運算子


i = 0
while i < 5:
    print(i)
    i += 1

i = 0
while i < 5:
    print(i)
    for j in range(5):
        print(j)
    if i == 3:
        break
    i += 1

import random

print(random.randrange(7))
print(random.randrange(1, 7))
print(random.randrange(1, 7, 2))

print(random.randint(1, 6))  # 包含1和6


# ans = random.randint(1, 100)
# while True:
#     num = int(input(f"請輸入1到100的數字: "))

#     if num < 0 and num > 100:
#         print("請輸入1到100的數字")
#     elif num < ans:
#         print("太大了")
#     else:
#         print("答對了!")
#         break


# 字典(dict)
# 字典是一個鍵值對的集合
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print(d)
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print(d["蘋果"])
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}

for k in d:
    print(k)
    print(d[k])

for k in d.keys():
    print(k)
    print(d[k])
for v in d.values():
    print(v)
for k, v in d.items():
    print(f"{k}:{v}")
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
d["蘋果"] = 10
print(d)
d["蓮霧"] = 15
print(d)

d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
d.pop("蘋果")


popitem = d.pop("蓮霧", "沒有這個鍵")
print(d)
print(popitem)
