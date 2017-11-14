d = {"a": 1, "b": 2, "c":3}
print(d)
print(d["a"])

d["d"] = 4
print(d["d"])
d["d"] = 5
print(d["d"])

print(d.get("e"))
print(d.get("e", "none"))

d.pop("d")
print(d)