"""
计算两个整数A和B的和。
"""

# 输入:输入有若干行，每行为由空格分隔的一对整数A和B，如： 5 12
while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break
# 输出：输出数据A和B的和



