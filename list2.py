#向下滑有输出结果
print("x原来的样子:", end="")
x = [1, 2, 3, 4, 5]
print(x)
print("append()添加单个对象")
x.append(6)
print(x)

print("extend()添加多个对象")
x = [1, 2, 3, 4, 5]
x.extend([1, 2])
print(x)

print("instert()插入对象")
x = [1, 2, 3, 4, 5]
x.insert(1, "123")
print(x)

print("remove()按值删除")
x = [1, 2, 3, 4, 5]
x.remove(2)
print(x)

print("pop()按位置删除")
x = [1, 2, 3, 4, 5]
x.pop()  # 默认为删除最后一个位置
print(x)
x.pop(1)  # 也可赋值删除
print(x)

print("clear()全部删除")
x = [1, 2, 3, 4, 5]
x.clear()
print(x)

print("-" * 10) #字符串可以乘法运算，具体看效果
print("x现在为:", [1, 2, 3, [1, 2], 5])

print("复制列表")
x = [1, 2, 3, [1, 2], 5]
y = x
print(y)
print("id:", id(y))
print("id:", id(x))

print("copy()复制列表")
x = [1, 2, 3, [1, 2], 5]
y = x.copy()
print(y)
print("id:", id(y))
print("id:", id(x))

print("deepcopy()复制列表")
import copy  # 导入copy库,不用太过在意，以后会讲

x = [1, 2, 3, [1, 2], 5]
y = copy.deepcopy(x)
print(y)
print("id:", id(y))
print("id:", id(x))

print("sort()全部删除")
x = [5, 4, 3, 1, 2]
print("原来：", x)
x.sort()
print("现在：", x)
x = ["hsd", "sadj", "suw", "sakj"]
print("原来：", x)
x.sort()
print("现在：", x)

'''
x原来的样子:[1, 2, 3, 4, 5]
append()添加单个对象
[1, 2, 3, 4, 5, 6]
extend()添加多个对象
[1, 2, 3, 4, 5, 1, 2]
instert()插入对象
[1, '123', 2, 3, 4, 5]
remove()按值删除
[1, 3, 4, 5]
pop()按位置删除
[1, 2, 3, 4]
[1, 3, 4]
clear()全部删除
[]
----------
x现在为: [1, 2, 3, [1, 2], 5]
复制列表
[1, 2, 3, [1, 2], 5]
id: 1802942493952
id: 1802942493952
copy()复制列表
[1, 2, 3, [1, 2], 5]
id: 1802942827072
id: 1802945340800
deepcopy()复制列表
[1, 2, 3, [1, 2], 5]
id: 1802945340800
id: 1802945356608
sort()全部删除
原来： [5, 4, 3, 1, 2]
现在： [1, 2, 3, 4, 5]
原来： ['hsd', 'sadj', 'suw', 'sakj']
现在： ['hsd', 'sadj', 'sakj', 'suw']
'''
