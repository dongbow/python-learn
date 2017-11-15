import math
from functools import reduce


def f(x):
    return x * x


r = map(f, [1, 3, 4, 5, 6, 7])

print(list(r))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

print(list(map(math.fabs, [-1, -2, -3])))


def add(x, y):
    return x * 10 + y


print(reduce(add, [1, 2, 3, 4, 5]))


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


print(reduce(add, map(char2num, '13579')))


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(fn, map(char2num, s))


print(str2int("12345"))


def str2int2(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2int2("12345"))


# ['adam', 'LISA', 'barT']
# ['Adam', 'Lisa', 'Bart']
def normalize(name):
    return map(lambda s: s.title(), map(lambda s: s.lower(), name))


name = normalize(['adam', 'LISA', 'barT'])
print(list(name))
