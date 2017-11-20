try:
    f = open("/Users/dongbo/Desktop/goods.txt", "r")
    print(f.read())
finally:
    f.close()

with open("/Users/dongbo/Desktop/goods.txt", "r") as f2:
    print(f2.read())


with open("/Users/dongbo/Desktop/goods.txt", "r", encoding="utf-8", errors="ignore") as f3:
    print(f3.read())


# writer
