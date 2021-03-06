import copy
"""
对于直接赋值，只引用了最外层对象的地址，所以，原始对象无论如何改动，都会跟着变动；
"""
"""
对于浅拷贝，只复制第一层的地址值,所以子对象（例如子列表）变化时，会跟随着一起变化；
"""
"""
而对于深拷贝，会复制内部所有的嵌套地址，所以已经完全独立出来了，不会随原对象变化而变化；
"""


a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象

b = a  # 赋值，传对象的引用
c = copy.copy(a)  # 对象拷贝，浅拷贝
d = copy.deepcopy(a)  # 对象拷贝，深拷贝

a.append(5)  # 修改对象a
a[4].append('c')  # 修改对象a中的['a', 'b']数组对象

print('原始列表      a = ', a)
print('直接赋值引用的 b = ', b)
print('浅拷贝        c = ', c)
print('深拷贝        d = ', d)
