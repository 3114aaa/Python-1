#往下滑有输出结果
a = []  # 创建空list
print("a", a)
a.append(1)  # 让a列表中添加1
print("a", a)

b = [1, 2, 3]  # list也可以直接赋值
print("b", b)

c = [1, "b", 3]  # list也可以有不同类型
print("c", c)

d = [1, [1, 2], "12"]  # list中还可以拥有list
print("d", d)

# 我们可以用[]取其中的值
print("d", d[2])

# 我们可以这样去多维数值
print("d", d[1][0])

# 我们也可以用list来拆分字符串
e = list("abcdef")
print("e", e)

# list也可以这样玩
f = list(range(-1, 10))
print("f", f)

g = list((1, 2, 3))
print("g", g)

# for创建list
h = list(x for x in range(5))
print("h", h)

# for的进阶玩法
i = list(x + 5 for x in range(5))
print("i", i)


'''
输出结果:
a []
a [1]
b [1, 2, 3]
c [1, 'b', 3]
d [1, [1, 2], '12']
d 12
d 1
e ['a', 'b', 'c', 'd', 'e', 'f']
f [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
g [1, 2, 3]
h [0, 1, 2, 3, 4]
i [5, 6, 7, 8, 9]
'''
