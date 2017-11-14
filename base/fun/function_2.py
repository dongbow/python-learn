# 情况1
def add_end(L=[]):
    L.append('END')
    return L


print(add_end([1, 2, 3]))

print(add_end())

print(add_end())  # ['END', 'END']


# 情况2
def add_end_o(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end_o())

print(add_end_o())  # ['END']


def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc([1, 2, 3]))

print(calc((1, 2, 3)))


# 可变参数
def calc_o(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc_o(1, 2, 3))

num = [1, 2, 3]
print(calc_o(*num))


# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


print(person('Michael', 30))
print(person('Bob', 35, city='Beijing'))
# print(person(person('Adam', 45, gender='M', job='Engineer')))

extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack', 24, **extra))