T = int(input())
for i in range(T):
    list = input().split()
    sum = 0
    if int(list[0]) == 0:
        break
    else:
        for j in list[1:]:
            sum += int(j)
        print(sum)

