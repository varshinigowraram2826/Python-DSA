def Name():
    a=10
    b=20
    print(a+b)
    print("kiran")
Name() #without par,return

def add(a,b):
    print(a+b)
    print("kiran")
#a=10
#b=20
#add(a,b)
add(10,20) #with par,without return

def add():
    a=10
    b=20
    
    return a+b
print(add()) #without par,with return

def add(a,b):
    return a+b
print(add("kiran","arjun"))
 print(add(10,20)) #with par and return

def greatest(a,b,c):
    if a>b and a>c:
        print(a,"is greater")
    elif b>a and b>c:
        print(b,"is greater")
    else:
        print(c,"is greater")
a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
greatest(a,b,c)

def power(n):
    m=1
    for i in range(1,n+1):
        m=m*2
    return m
#n=int(input("enter power"))
power(5)

def fact(a):
    c=1
    for i in range(1,a+1):
        c=c*i
    print(c)
a=int(input("enter number"))
fact(a)

def fib(n):
   a=0
   b=1
  # print(a)
  # print(b)
   for i in range(n):
       c=a+b

       a=b
       b=c
   print(c)
n=int(input("enter series"))  
fib(n)

def fib(n):
    if n<=0:
        return 0
    if n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input("enter series"))
a=fib(n)
print(a)
