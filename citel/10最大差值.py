"""
给定一个整数数组，请求出该数组中两数之差（绝对值）的最大值。要求单独定义函数实现。
"""

def func(n, list):
    for i in list:
        i = int(i)
        list_int.append(i)
    list_int.sort()
    print(list_int[n-1] - list_int[0])

# 输入:第一行为一个正整数n,随后第二行为n个整数
n = int(input())
list = input().split()
list_int = []
func(n, list)
# 输出：该数组中两数之差（绝对值）的最大值