"""
有N张卡牌，每张卡牌上标记有一个正整数。为管理方便对卡牌按数值大小进行了从小到大的排序，现希望知道是否存在标记有某个数值的卡牌，以及其排序后的位置。排序后第一张卡牌的位置记为1，以此类推，第N章卡牌的位置记为N。
"""

# 输入:输入有多组数据，每组数据包含三行整数，第一行为空格分隔的两个正整数N,Q，分别表示卡牌张数和问题数，第二行为卡牌上的数值，第三行为Q空格分隔查询的数值
T = 1
while True:
    try:
        n, q = map(int, input().split())
        data = list(map(int, input().split()))
        find = list(map(int, input().split()))
        data_sort = sorted(data)
        print(f"Case #{T}:")
        for i in find:
            try:
                x = data_sort.index(i)
                print(f"{i} found at {x+1}")
            except:
                print(f"{i} not found")
        T += 1
    except:
        break
# 输出：对每组数据，第一行输出Case #T:，其中T为当前数据组的编号，从1开始； 随后对每个查询单独输出一行。若存在该编号，输出q found at x，q为查询编号的数值，x为其排序后的位置；若不存在，输出q not found，q为查询的数值



