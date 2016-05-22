__author__ = 'X'

#def fib(x):
#    if x ==1 or x ==2:
#        return 1
#    else:
#        return fib(x-1) + fib(x-2)
#x = 1
#while True:
#    if len(str(fib(x))) > 1000:
#        break
#print(fib(x),x)

a = 1
b = 1
index = 2
while len(str(b)) < 1000:
    a,b = b, a+b
    index += 1
print(index)

import webbrowser
webbrowser.open('http://www.baidu.com')