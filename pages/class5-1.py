d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print(len(d))

d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print("蘋果" in d)
print("蓮霧" in d)

l = [1, 2, 3, 4, 5]
print(3 in l)

d = {"a": [1, 2, 3], "b": {"c": 4, "d": 5}}
print(d["a"])
print(d["a"][0])
print(d["b"])
print(d["b"]["c"])


grade = {
    "小明": {"國文": [90, 80, 70], "數學": [78, 90, 80], "英文": [90, 80, 70]},
    "小美": {"國文": [80, 70, 60], "數學": [90, 80, 70], "英文": [80, 70, 60]},
    "小華": {"國文": [70, 60, 50], "數學": [90, 80, 70], "英文": [70, 60, 50]},
}

print(grade["小明"]["數學"])

print(grade["小美"]["英文"][0])

print(grade["小華"]["國文"][1])
