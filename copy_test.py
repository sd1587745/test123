__author__ = 'X'
import copy
a = [1,2,'a',['a','b']]
b = a
c = copy.copy(a)
print(a)
print(b)
print(c)
a.append('c')
print(id(a[1]))
print(id(c[1]))

a[1] = 5
print(id(a[1]))
print(id(c[1]))

a[3].append('test')
print(a)
print(b)
print(c)
