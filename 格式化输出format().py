# 格式化输出format()
print("名字:{},年龄:{}".format("tom", 16))

# 自定义顺序
print("名字:{1},年龄:{0}".format("tom", 16))

# 定义变量
print("名字:{name},年龄:{age}".format(name="tom", age=16))
'''
%d,%i 整形
%o 八进制
%x %X 十六进制
%e 科学计数e
%E 科学计数E
%f 小数
%c asc码
%s 字符串
'''
print("年纪:%d" % (123))
