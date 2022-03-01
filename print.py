#print([obj1],[obj2]...[,sep=""][,"endl=""][,file=sys.stdout])

print("a","b","c")
print("a", "b", "c", sep="")
print("a", "b", "c", sep="#")
#比较上面三个打印的区别

print("abc")
print("def", end="")
print("g")
#观察有end与没有的区别

wf = open("t.txt", "w")
print("123", file=wf)#t.txt写入“123”
wf.close()
#观察项目文件夹下是否生成t.txt,内容是否为"123"
