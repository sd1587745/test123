__author__ = 'X'
import random
#pool = range(1000)
#randpool = random.sample(pool,1000)
import sys
sys.setrecursionlimit(1000000)
randpool = [86, 59, 18, 81, 19, 62, 83, 94, 64, 93, 35, 37, 13, 90, 51, 79, 22, 71, 21, 3]
x1= randpool
x2= randpool
x3= randpool
x4= randpool

print(randpool)
#def bubble(li):
#    ind = 1
#    length = len(li)
#    while True:
#        i = 0
#        tag = 0
#        while i < length-1:
#            if li[i] > li[i+1]:
#                li[i], li[i+1] = li[i+1], li[i]
#                tag = 1
#                print(li,ind)
#                ind += 1
#            i += 1
#        if tag == 0:
#            break
#    return li
#
#print(bubble(x1))


#def bubblesort(data):
#    ind = 1
#    for i in range(len(data) - 1, 0, -1):
#        for j in range(0, i):
#            if data[j] > data[j + 1]:
#                data[j], data[j + 1] = data[j + 1], data[j]
#                print(data,ind)
#                ind += 1
#
#bubblesort(x2)
#print(x2)
#
#def select(li):
#    length = len(li)
#    i = 0
#    ind =1
#    while i < length - 1:
#        temp = 0
#        mini = li[i]
#        for x in range(i, length):
#            if li[x] < mini:
#                mini = li[x]
#                temp = x
#        if temp != 0:
#            li[i], li[temp] = li[temp], li[i]
#            print(li,ind)
#            ind += 1
#        i+= 1
#    return  li
#print(select(x2))



#def bubbleSort(a):
#    l=len(a)-2
#    i=0
#    while i<l:
#        j=l
#        while j>=i:
#            if(a[j+1]<a[j]):
#                a[j],a[j+1]=a[j+1],a[j]
#            j-=1
#        i+=1
#
#print(bubble(x3))

def quick(x,i=0, j=None):
    if j==None:
        j = len(x) - 1

    m = i
    n = j

    if i < j:

        while i < j:
            while x[j] >= x[m] and j > i:

                j -= 1
            while x[i] <= x[m] and j > i:

                i += 1
            x[i], x[j] = x[j], x[i]

        x[m], x[i] = x[i], x[m]
        quick(x, m, i-1)
        quick(x, i+1, n)

quick(x4)
print(x4)
