list = ["a", "b", "c"]
print(list)
print(len(list))
print(list[2])
print(list[-1])
list.append("d")
print(list)
list.insert(0, "a")
print(list)
list.pop()
print(list)
list.pop(0)
print(list)
list[1] = "aa"
list[2] = "aaa"
print(list)

list2 = ["a", "b", 1, ["a", "b", 2]]
print(list2)
print(list2[3][1])
list2[3].append("c")
print(list2[3])
print(len(list2))
print(len(list2[3]))

list = [1, 3, 5, 4, 7, 8, 3, 0]
list.sort()
print(list)
