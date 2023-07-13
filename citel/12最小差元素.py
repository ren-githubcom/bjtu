"""
给定一个整数数组，请求出该数组中两数之差（绝对值）的最小值，并确定对应元素的位置。
"""

# 输入:第一行为一个正整数n,随后第二行为n个整数
n = int(input())
l = input().split()
l1 = list(map(int, l))

l_sort = sorted(l1)
l_diff = []
for i in range(n-1):
    diff = abs(l_sort[i+1] - l_sort[i])
    l_diff.append(diff)
# 找到最小差的位置
min_diff = l_diff.index(min(l_diff))
x1 = l1.index(l_sort[min_diff])
x2 = l1.index(l_sort[min_diff+1])
# 若存在两数相同，则
if x1 == x2:
    x2 = l1.index(l_sort[min_diff+1], x1+1)
# 输出：该数组中两数之差（绝对值）的最小值及对应元素在输入数组中的位置索引，索引从1开始计数，以空格分隔。若有多组，输出任意一组即可。
print(min(l_diff), x1+1, x2+1)