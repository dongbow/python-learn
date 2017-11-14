from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(d.get(key))

for value in d.values():
    print(value)

print(isinstance('abc', Iterable))


for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)