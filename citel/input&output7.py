while True:
    try:
        list = input().split()
        sum = 0
        for i in list:
            sum += int(i)
        print(sum)
        print()
    except:
        break