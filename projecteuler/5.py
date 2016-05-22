__author__ = 'X'


def small(x):
    y = 2
    while y != 4:
        if x % y:
            x += 1
            small(x)
        else:
            y += 1
    return x

print(small(10))



