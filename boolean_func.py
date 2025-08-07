def is_between(x, y, z):
    return x <= y <= z or z <= y <= x

print(is_between(1, 2, 3))  # True
print(is_between(3, 2, 1))  # True
print(is_between(1, 3, 2))  # False