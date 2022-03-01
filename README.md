## 一.print的使用

>[代码参考](https://github.com/3114aaa/Python/blob/main/print.py)

<details><summary>格式查看</summary>
<p>
  print([obj1],[obj2]...[,sep=""][,"end=""][,file=sys.stdout])
  
  obj表示内容，sep用于替换obj与obj的逗号（逗号默认输出为空格），end结尾替换（print默认结尾会换行），file为打开文件对象(打开文件代码为'''变量名 = open("路径","w")''')
  
</p>
</details>

## 二.定义变量及其类型的识别

>[代码参考](https://github.com/3114aaa/Python/blob/main/%E5%8F%98%E9%87%8F%E7%B1%BB%E5%9E%8B.py)

python中定义变量格式: 变量名 = 值 （python会自动识别变量名)

<details><summary>进阶学习</summary>
<p>
  函数:type()可以识别变量类型，见代码参考中
</p>
</details>

## 三.if语句，input函数的学习

>[代码参考](https://github.com/3114aaa/Python/blob/main/if%E7%9A%84%E4%BD%BF%E7%94%A8.py)

python if语句和VB一样

<details><summary>格式查看</summary>
<p>
  <b>第一种使用</b>

    if 条件判断：
      执行代码
  
  <b>第二种使用</b>
  
    if 条件判断：
      执行代码A
    else:
      执行代码B
    
  <b>第三种使用</b>
  
    if 条件A判断：
      执行代码A
    elif 条件B判断:
      执行代码B
    ...
    else:
      执行代码B
  
  <b><i>相信能看我写博客的人都学过VB，与VB知识差不多的就不过多叙述了</i></b>
  
</p>
</details>

ps:参考代码中有输入代码input,用于用户输入内容，不管用户输入什么都为字符串，例如用户输入123，
python会默认"123",因此eval()函数是将最外边的双引号或引号去了，例如eval("123")等于123，eval("1+2")等于3（因为去了引号后为1+2，不是字符串，于是python就开始运算了） 

## 四.格式化输出format()函数

>[代码参考](https://github.com/3114aaa/Python/blob/main/%E6%A0%BC%E5%BC%8F%E5%8C%96%E8%BE%93%E5%87%BAformat().py)
>没有固定格式，具体看代码

<details>
  <summary>和format功能类似</summary>
  <p>
  
    %d,%i 整型
  
    %o 八进制
  
    %x %X 十六进制
  
    %e 科学计数e
  
    %E 科学计数E
  
    %f 小数
  
    %c asc码
  
    %s 字符串
  
用法(例如输出整型)：print("年龄:%d"%(18))
  
  输出结果：年龄:18
  
  ps:可以试着写写</p></details>
   
# 五.关于数值型
  ## （1）二、八、十六进制转十进制
  
  ## （2）数值的运算符
  符号|作用|符号|作用
  ----|----|----|----
    + | 加 | << | 移位
    - | 减 | >> |移位
    * | 乘 |  & |按位与
    / | 除 |竖线|按位或
   // |整除| 无 | 无
   ** | 幂 | 无 | 无 
    % |取余| 无 | 无 

   
    
    
  
  ## （3）

判断语句用到的运算符
<> => <= == !=
not and or
'''
'''

关于数字的函数
abs() 绝对值
之后慢慢加
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
