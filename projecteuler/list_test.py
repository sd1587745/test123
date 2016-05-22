__author__ = 'X'


def CheckKey(key):
    if not isinstance(key,int):
        raise TypeError
    if key < 0:
        return IndexError


class MakeupList(object):

    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.storage = {}

    def __getitem__(self, key):
        CheckKey(key)
        try:
            return self.storage[key]
        except KeyError:
            return self.start + self.step * key

    def __setitem__(self, key, value):
        CheckKey(key)
        self.storage[key] = value


check = MakeupList(1, 2)
print(check[8])
check[8] = 100
print(check[8])

for x in range(0, 15):
    print(check[x])



chec