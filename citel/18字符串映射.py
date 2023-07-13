"""
有两个长度相同的字符串，均由字母A-Z构成，长度不超过100。请判断是否可以把其中一个字符串的各个字母重排，然后对26个字母做一个一一映射，使得两个字符串相同。
"""

def func(a):
    """
    得到统计每个字母出现的次数的字典和数组
    :param a: 输入的字符串
    :return: 次数字典和数组
    """
    a_set = set(a)  # 去重
    a_list = list(a_set)   # 去重后存入数组
    cnt_s = {}
    cnt_l = []
    for i in a_list:
        s = 0
        for j in a:
            if i == j:
                s += 1
        cnt_s[i] = s
        cnt_l.append(s)
    return cnt_s, cnt_l

# 输入:两行字符串
a = input()
b = input()
cnt1_s, cnt1_l = func(a)
cnt2_s, cnt2_l = func(b)
if sorted(cnt1_l) == sorted(cnt2_l):
    print("YES")
    cnt1_s = sorted(cnt1_s.items(), key=lambda x: x[1], reverse=True)
    cnt2_s = sorted(cnt2_s.items(), key=lambda x: x[1], reverse=True)
    for i in range(len(cnt1_s)):
        print(f"{cnt1_s[i][0]}->{cnt2_s[i][0]}", end=" ")
else:
    print("NO")
# 输出：若可以请输出两行，第一行为YES，第二行为对应的一个映射。否则输出NO。



