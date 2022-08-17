import math
from time import time


def timer(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'\nFunction "{func.__name__}" executed in {math.ceil((t2 - t1) * 1000)}ms')
        return result

    return wrap_func
