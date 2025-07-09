print([])  # 這是一個空的list
print([1, 2, 3])  # 這是一個包含3個數字的list
print([1, 2, 3, "a", "b", "c"])  # 這是一個包含6個元素的list
print([1, 2, 3, ["a", "b", "c"]])  # 這是一個有4個元素的list
print([1, True, "a", 1.23])  # 這是一個有4個元素的list

# list 讀取元素,元素的index從0開始
l = [1, 2, 3, "a", "b", "c"]

# LIST 取長度 , 也就是List元素
l = [1, 2, 3, "a", "b", "c"]
print(len(l))  # 6

# LIST 走訪元素
# 可以透過index的方式來找到list中的資料
l = [1, 2, 3, "a", "b", "c"]
for i in range(0, len(l), 2):
    print(l[i])

for i in l:
    print(i)


# list 修改元素
# 可以透過index來修改list中的元素
l = [1, 2, 3, "a", "b", "c"]
l[0] = 2  # 把index为0的元素改成2
print(l)

# call by value
a = 1
b = 2  # 複製a的值給b
b = 2
print(a, b)  # a還是1 , b變成2


# call by reference
a = [1, 2, 3]
b = a  # 把a跟b指向同一個記憶體位置,所以改變b的值 , a也會跟著改變
b[0] = 2
print(a, b)

a = [1, 2, 3]
b = a.copy()
b[0] = 2
print(a, b)

# list的append ,也就是在list後面加入元素
l = [1, 2, 3]
l.append(4)  # 把4加到l的最後
print(l)

# list的移除元素方式有兩種
# 1. 使用remove ,可以移除指定的元素
l = ["a", "b", "c", "d"]
l.remove("b")  # 移除b
for i in l:
    if i == "b":
        l.remove(i)

# sort:將list中的元素排序  ,由小到大
# 注意:這個方法會改變list的元素
l = [1, 2, 3, 4, 5]
l.sort()
print(l)


# open() 開啟檔案
# r - 讀取模式
# w - 寫入模式
# a - 追加模式
# r+ - 讀取寫入模式
# w+ - 讀取與寫入模式
# a+ - 讀取

# 開啟檔案
# 絕對路徑  C:/Users/wuaxe/Desktop/pythonxai/pages/class1-1.py
# 相對路徑  pages/class1-1.py
f = open("pages/class1-1.py", "r", encoding="utf-8")
content = f.read()
print(content)
f.close()

# 字串的小工具
filename = "class1.md"
print(filename.endswith(".md"))
filename2 = "notes.txt"
print(filename2.endswith(".md"))
