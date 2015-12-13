[x ** 2 for x in range(1, 11)]  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# List comprehension with conditional
[x ** 2 for x in range(1, 11) if x % 2 == 0]  # [4, 16, 36, 64, 100]

mapped = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(1, 11)))
mapped  # [4, 16, 36, 64, 100]
