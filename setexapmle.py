# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 12:10:41 2019

@author: Bharathi
"""
#for union and update  join
print("hello")
x={"apple","banana","mango"}
y={1,2,3,4}
z=x.union(y)
print(z)
print("banana" in x)
x.update(y)
print(x)

#for set constructor
a=set(("Apple",2,3,5,"mango"))
print(a)
for x in a:
    print(x)
   # print("banana" in x)
#for add and update
x={"apple","banana","mango"}
print(x)
print(y)
x.add("orange")
print(x)
x.update([1,2,3,"graphs"])
print(x)
print(len(x))
x.remove("banana")
print(x)
#print(x.remove("mango"))
x.remove("mango")
print(x)   
x.discard("apple")
print(x)


x = 10

x ^= 3

print(x)
x**=3
def abc(x):
    return 10*x
    print("hello world")
print(abc(4))
def a(*y):
    print(y[2])
a("q","s","a")
x=lambda a,b:a+b
print(x(2,3))
y=lambda a,c,b:a+b*c
print(y(1,2,3))
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

   
    