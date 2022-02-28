#print([obj1],[obj2]...[,sep=""][,"endl=""][,file=sys.stdout])
print("a", "b", "c", sep="")
print("def", end="")
wf = open("t.txt", "w")
print("123", file=wf)#t.txt写入“123”
wf.close()
