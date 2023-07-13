"""
有两个长度相同的字符串，均由字母A-Z构成，长度不超过100。请判断是否可以把其中一个字符串的各个字母重排，然后对26个字母做一个一一映射，使得两个字符串相同。
"""

# 统计每个字母出现的次数
# 得到两个数组
# 判断两个数组排序之后的结果是否相同
def func(a):
    """
    得到统计每个字母出现的次数的数组
    :param a: 输入的字符串
    :return: 次数数组
    """
    a_set = set(a)  # 去重
    a_list = list(a_set)   # 去重后存入数组
    cnt = []
    for i in a_list:
        s = 0
        for j in a:
            if i == j:
                s += 1
        cnt.append(s)
    return cnt

# 输入:两个字符串，以空格分隔
a = input()
b = input()
cnt1 = func(a)
cnt2 = func(b)
if sorted(cnt1) == sorted(cnt2):
    print("YES")
else:
    print("NO")
# 输出：若可以请输出YES，否则输出NO