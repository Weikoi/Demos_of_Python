from collections.abc import Iterator, Iterable

a = (i for i in range(10))

print(isinstance(a, Iterator))