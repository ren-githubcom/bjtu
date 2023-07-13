"""
有一个整数序列，序列中每个元素的质因数只有2,3,5，该序列的前几个元素为1,2,3,4,5,6,8,10...。按惯例，1也作为序列中的元素，且是序列中的第一个元素。现在感兴趣的是，给定一个位置n(1≤n≤10000)，该序列中第n个元素是多少？
"""

# 输入:输入有若干行，每行为一个整数n，为查询的元素位置。
while True:
    try:
        n = int(input())
        l = []
        if n == 1:
            print(n)
            l.append(n)
        else:
            if n//2==1 :
                l.append(n)
            elif n%3==0 or n%3==2 or n%3==5:
                l.append(n)
            elif n%5==0 or n%5==2 or n%5==3:
                l.append(n)
            else:
                pass
            print(l)

    except:
        break
# 输出：对每行输入，在单独的行中输出序列中对应位置的元素。


