__author__ = 'X'


def fib(x):
    i = 2
    while x != i:
        if not x % i:
            x /= i
            fib(x)
        else:
            i += 1
    return x

print(fib(600851475143))












