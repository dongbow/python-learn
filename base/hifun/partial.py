import functools

print(int('12345', base=16))


int2 = functools.partial(int, base=2)

print(int2('10010'))