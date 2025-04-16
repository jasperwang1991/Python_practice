
s = "first line, \nsecond line"   # \n 換行符
# print(s)

n = "first line, \\nsecond line"   # \ 轉義字符
# print(n)

t = r"first line, \nsecond line"   # r 原樣輸出
# print(t)

x = 5 * 'un' + 'ttt'    # 字符串可以* 也可以+
# print(x)

# print('a'   "b")    # 相鄰的字符串會自動合并到一起 這個功能很實用
# print(3 * 'r' "4")  # 先拼接再作乘

# print(x + "44444")

# 字符串的索引和切片 索引包含負值索引
p = 'Python'
# print(p[3])
# print(p[0:2])
# print(p[:])
# print(p[-1])
# print(p[-2:])
# print(p[:-2])
# print(p[-4:-2])
# print(p[45])   # 超過字符串長度會報錯
print(p[45:78])   # 切片時超過長度不會報錯

# p[3] = "444"   # 字符串的值不能更改 只能重新定義

print(len(p))   # 内置函數 返回字符串的長度
