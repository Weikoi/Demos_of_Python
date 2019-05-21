from collections.abc import Iterator, Iterable

# 生成器即是可迭代对象， 也是迭代器
a = (i for i in range(10))

print(isinstance(a, Iterable))
print(isinstance(a, Iterator))

# 列表是可迭代对象，但是不是迭代器
b = [i for i in range(10)]

print(isinstance(b, Iterable))
print(isinstance(b, Iterator))
