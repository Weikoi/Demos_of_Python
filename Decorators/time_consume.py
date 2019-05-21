import time

"""
一个记录函数运行时间的装饰器
"""


def metric(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = fn(*args, **kwargs)
        time.sleep(1)  # 这里是故意延时一秒以显示装饰器效果。
        end = time.time()
        print('%s executed in %s s' % (fn.__name__, round(end - start, 3)))
        return res

    return wrapper


def func(a, b):
    return a + b


@metric
def func2(a, b):
    return a + b


if __name__ == '__main__':
    # 使用函数闭包的写法
    func = metric(func)
    print(func(1, 2))

    # 使用语法糖写法，直接在func上方标注@metric
    print(func2(1, 2))
