**print的使用**
`#print([obj1],[obj2]...[,sep=""][,"endl=""][,file=sys.stdout])
print("a", "b", "c", sep="")
print("def", end="")
wf = open("t.txt", "w")
print("123", file=wf)#t.txt写入“123”
wf.close()`


'''
\n  换行
\t  tab
\\  \
#\'  '
#\"  "
\0  空
\ooo    八进制
\xhh    十六进制
'''
