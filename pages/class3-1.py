# 連續使用if跟使用if  elif  else的差別
# elif 可以排除前面有判斷的條件
# 但是如果使用多個if來做讀立判斷

# for 迴圈
# for迴圈可以從一個列表中取出每個元素並且做事情
# range(5)會產生 [0,1,2,3,4]
for i in range(5):
    print(i)
    print("holle")

    # range 可以設定起始值與結束值， 但不會包含結束值
    # range(1, 5)會產生 [1,2,3,4]
    for i in range(1, 5):
        print(i)

        # range 可以設定起始值與結束值， 但不會包含結束值
        # range(1, 10, 2)會產生 [1,3,5,7,9]
        for i in range(1, 10, 2):
            print(i)
