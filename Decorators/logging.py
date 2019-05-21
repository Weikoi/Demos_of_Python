import time

"""
一个打本地日志的装饰器
"""


def logging(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = fn(*args, **kwargs)
        end = time.time()

        # 在本地打印log,记录函数的运行历史记录
        with open("log.txt", 'a') as f:
            line = "excute in %f s   @   " % (end - start) + time.strftime('%Y-%m-%d, %H:%M:%S\n',
                                                                           time.localtime(time.time()))
            f.write(line)
        print("time using:", end - start)
        return res

    return wrapper


@logging
def func(a, b):
    return a + b


if __name__ == '__main__':
    func(1, 2)
