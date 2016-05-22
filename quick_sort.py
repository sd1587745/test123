__author__ = 'X'

import random
#import sys
#sys.setrecursionlimit(1000000)
#x = range(10)
#y = random.sample(x,10)
#x = [6, 5, 0, 7, 2, 9, 3, 8, 4, 1]
#x=[  0 , 1, 2, 4]

pool = range(1000)
x = random.sample(pool, 1000)
print(x)


def quick(x,i=0, j=None):
    if j==None:
        j = len(x) - 1

    m = i
    n = j

    if i < j:

        while i < j:
            while x[j] >= x[m] and j > i:
                print(i, j, 1)
                j -= 1
            while x[i] <= x[m] and j > i:
                print(i,j,2)
                i += 1
            x[i], x[j] = x[j], x[i]
        print(i, j)
        x[m], x[i] = x[i], x[m]
        quick(x, m, i-1)
        quick(x, i+1, n)

quick(x)
print(x)



#def Partition(mylist, low, high):
#    tmp = mylist[low]
#    while low < high:
#        while low < high and mylist[high] >= tmp:
#            high = high - 1
#        if low < high:
#            mylist[low] = mylist[high]
#            low = low + 1
#        while low < high and mylist[low] <= tmp:
#            low = low + 1
#        if low < high:
#            mylist[high] = mylist[low]
#            high = high - 1
#    mylist[low] = tmp
#    return low
#def QuickSort(mylist, low, high):
#    if low < high:
#        pivotpos = Partition(mylist, low, high)
#        QuickSort(mylist, low, pivotpos - 1)
#        QuickSort(mylist, pivotpos + 1, high)
#
#QuickSort(x, 0, len(x) - 1)
#print(x)

def quicksort(data, low = 0, high = None):
    if high == None:
        high = len(data) - 1
    if low < high:
        s, i, j = data[low], low, high
        while i < j:
            while i < j and data[j] >= s:
                j = j - 1
            if i < j:
                data[i] = data[j]
                i = i + 1
            while i < j and data[i] <= s:
                i = i + 1
            if i < j:
                data[j] = data[i]
                j = j - 1
        data[i] = s
        quicksort(data, low, i - 1)
        quicksort(data, i + 1, high)

#quicksort(x)
#print(x)
