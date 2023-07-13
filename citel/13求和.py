"""
计算若干十六进制数的和。
"""

# 输入:输入有若干行，每行为由空格分隔的若干数十六进制整数
while True:
    try:
        data = input().split()
        data1 = list(map(lambda x: int(x, 16), data))
        sum = 0
        for i in data1:
            sum += i
        print(sum)
    except:
        break
# 输出：控制台输出，对每行输入，输出该行十六进制数的和，用十进制表示