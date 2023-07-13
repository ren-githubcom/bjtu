"""
请将格式如yyyy-m-d形式的日期转换为mm/dd/yyyy格式表示的日期。
"""

# 输入:若干行，每行为一个yyyy-m-d形式的日期
while True:
    try:
        data = input()
        l = data.split("-")
        print("%02d/%02d/%04d" % (int(l[1]), int(l[2]), int(l[0])))
    except:
        break
# 输出：对每行输入的日期，将其转换为mm/dd/yyyy格式表示的日期