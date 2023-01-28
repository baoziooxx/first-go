#l=[]
#n=1
#while n<99:
#    l.append(n)
#    n=n+2




from curses import KEY_MARK
from functools import reduce
from re import A, S
from readline import insert_text
from telnetlib import X3PAD
from tkinter import N, W


def check(l):
    n=0
    while n <len(l):
        if l[n]!=' ':
            l=l[n:(len(l)+1)]
            break
        else:
            n=n+1
 #   print('此时l=',l,'对吧')

    while n<len(l):
        if l[n]==' ':
            l=l[:n]
            break
        else:
            n=n+1

    return l



def ins(x):
    if x==[]:
        a=None
        b=None
    else:
        a=x[0]
        b=x[0]
        for i in x:
            if i>=a:
                a=i
            if i<=b:
                b=i

    return (b,a)
        

def yang(x):
#    de=[1]
#    if x==1:
#        print(de)
#    elif x==2:
#        print(LL)
    LL=[1]
    n=1
    while n<x:
        #print('此时LL=',LL)
        LLL=[1]
        a=0
        b=1
        while b<len(LL):
            ins=LL[a]+LL[b]
            LLL.append(ins)
            a=a+1
            b=b+1
        if n!=1:
            LLL.append(1)
        print (LLL)
        n=n+1
        LL=LLL
        #print('准备下一次，LL=',LL)

    
def yang2(x):

    LL=[1]
    n=1
    while n<x:
        #print('此时LL=',LL)
        LLL=[1]
        a=0
        b=1
        while b<len(LL):
            ins=LL[a]+LL[b]
            LLL.append(ins)
            a=a+1
            b=b+1
        if n!=1:
            LLL.append(1)
        yield LLL
        n=n+1
        LL=LLL
        #print('准备下一次，LL=',LL)

    

def yang3():

    LL=[1]
    n=1
    while n:
        #print('此时LL=',LL)
        LLL=[1]
        a=0
        b=1
        while b<len(LL):
            ins=LL[a]+LL[b]
            LLL.append(ins)
            a=a+1
            b=b+1
        if n!=1:
            LLL.append(1)
        yield LLL
        n=n+1
        LL=LLL
        #print('准备下一次，LL=',LL)


def normalize_name(a):#接收一个单词
    def f(b):#单字母若为大写，转为小写
        if ord(b)<91:
            b=chr(ord(b)+32)
        return b#必须return，否则map接收不到值
    a=list(map(f,a))  
    if ord(a[0])>96: #将首字母转换为大写
        a[0]=chr(ord(a[0])-32)
    return ''.join(a)

def prod(x):
    def pp(x,y):
        s=x*y
        return s

    a=reduce(pp,x)
    return a

def str2(x):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':'.'}

    #转换为list
    #用map，除了.，每个字符转换为数字
    def fir(a):
        return DIGITS[a]
    m1=list(map(fir,list(x)))
   
    #除以10的n次方，n=len（x）-.索引-1
    for k,v in enumerate(m1):
        if v=='.':
            n=k
    
 #   print('len m1=',len(m1),'n=',n)
    
    # 用reduce*10+后一个
    def plus(b,c):
        s=b*10+c
        return s
    m1.pop(n)
    m2=reduce(plus,m1)
 #   print('m2=',m2)
 #   print('tt=',tt,'len(m1)=',len(m1))
    m3=m2/(10**((len(m1))-n))
    return m3


def num(x):
    b=x
    L=[]
    while x!=0:
        a=x%10
        x=(x-a)*0.1
        L.append(a)

    def pl(x,y):
        return x*10+y
    
    k=reduce(pl,L)
   # print('k=',k,'b=',b)
    return b==k

def by_name(x):
    return x[0]

def by_score(x):
    return x[1]












def baba(x):
    import math

    n=1
    a=0
    while n <= x:
        
        y=(x-n)*math.pow(0.01,(x-n))*math.pow(0.99,n)
        n=n+1

        a=a+y
    b=a+math.pow(0.01,x)
    return b

def bab(x):
    import math
    a=0.01**4
    aa=math.pow(0.01,4)
    b=3*0.01**3*0.99
    bb=3*math.pow(0.01,3)*0.99
    c=2*0.01**2*0.99**2
    cc=2*math.pow(0.01,2)*math.pow(0.99,2)
    d=0.01*0.99**3
    dd=0.01*math.pow(0.99,3)
    print(a,aa,b,bb,c,cc,d,dd)
    print(a+b+c+d)
    print(aa+bb+cc+dd)
    0
    return 