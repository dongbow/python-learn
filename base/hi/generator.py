g = (x * x for x in range(10))
print(g)

print(next(g))
print(next(g))

for i in g:
    print(i)


def fib(x):
    n, a, b = 0, 0, 1
    while n < x:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib(6))

f = fib(6)
print(f)