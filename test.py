__author__ = 'X'
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
        return
    move(n-1, a, c, b)
    print('move', a, '-->', c)
    move(n-1, b, a, c)

move(2, 'A', 'B', 'C')


a = list(range(1,10))
print(a)


print([x * x for x in range(1, 11)])
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])


from functools import reduce


def f(a, b):
    return a+b
L = ['a', 'b', 'c', 'd', 'e','f']
print(reduce(f,L))
print('Thanks','My love')
print(L.pop(2))

print(L[3])


abc = '123465'
try:
    print(abc)
except NameError:
    print('Name error in line 35')

dic = {'a' : [], 'b':'good'}

dic['a'].append(2)
del dic['b']


class test(object):
    def __init__(self,key):
        self.key = key

a = test('abd')

l=[1,2,3,5,8,4,7]
l.sort()
print(l)
lm = {1:1,2:2,3:5}
print(lm.values())
