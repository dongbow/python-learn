l = [1, 2, 3, 4, 6, 5, 7, -3]
print(sorted(l))
print(sorted(l, reverse=True))

print(sorted(l, key=abs))

s = ['a', 'sdf', 'fg']
print(sorted(s))

s1 = ("a", 'b', 'd', 'c')
print(sorted(s1))
