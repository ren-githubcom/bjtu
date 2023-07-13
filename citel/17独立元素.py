"""
给定一个整数数组，请按从大到小的顺序输出该数组中元素，相同的元素只输出一次。
"""

# 输入:第一行为一个正整数N(1<N≤10000)，随后第二行为N个整数，整数间以空格分隔
n = int(input())
data = input().split()
data_int = list(map(int, data))
data_int.sort(reverse=True)
data_new = []
for i in range(n):
    if i == 0:
        data_new.append(data_int[i])
    else:
        if data_int[i] == data_int[i-1]:
            continue
        else:
            data_new.append(data_int[i])

# 输出：按从大到小的顺序输出满足条件的元素
for i in data_new:
    print(i, end=' ')


