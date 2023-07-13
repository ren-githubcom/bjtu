"""
请通过函数实现，输出底边长为n的镂空等腰三角形。
"""
def func(c, n):
    for i in range(n):
        if i == 0:   # 第一行
            for j in range(n - i - 1):
                print("", end=" ")
            print(c, end=" ")
        elif i == n-1:   # 最后一行
            for j in range(i + 1):
                print(c, end=" ")
        else:   # 中间行
            for j in range(n - i - 1):
                print("", end=" ")
            print(c, end=" ")
            for k in range(2 * i - 2):
                print("", end=" ")
            print(c, end=" ")
        print()

# 输入:标准输入，包括两部分：c,n(0,100],c为指定输出的ASCII字符,n为指定的边长
c, n = map(str, input().split())
n = int(n)
# 输出：用指定的字符输出边长为n的镂空等腰三角形
func(c, n)
