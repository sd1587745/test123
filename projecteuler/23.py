__author__ = 'X'
def abundant(x):
    sum_ = 0
    for _ in range(1, x):
        if not x % _:
            sum_ +=_
    return sum_

print(abundant(14062))