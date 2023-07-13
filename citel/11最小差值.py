"""
给定一个整数数组，请请求出该数组中两数之差（绝对值）的最小值。要求单独定义函数实现。
"""

def func(n, list_int):
    list_int.sort()
    min_diff = float('inf')
    for i in range(n-1):
        diff = abs(list_int[i+1] - list_int[i])
        min_diff = min(diff, min_diff)
    return print(min_diff)

# 输入:第一行为一个正整数n,随后第二行为n个整数
n = int(input())
list_in = input().split()
list_int = list(map(int, list_in))
func(n, list_int)
# 输出：该数组中两数之差（绝对值）的最小值