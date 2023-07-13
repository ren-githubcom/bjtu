while True:
    list = input().split()
    sum = 0
    if int(list[0]) == 0:
        break
    else:
        for i in list:
            sum += int(i)
        print(sum)