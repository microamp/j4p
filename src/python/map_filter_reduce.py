import functools
import operator

mapped = map(lambda x: x * 2, range(1, 6))
list(mapped)  # [2, 4, 6, 8, 10]

filtered = filter(lambda x: x % 2 == 0, range(1, 11))
list(filtered)  # [2, 4, 6, 8, 10]

functools.reduce(operator.add, range(1, 5))  # 10
