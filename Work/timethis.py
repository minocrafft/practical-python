from time import time


def timethis(func):
    def wrapper(*args, **kwargs):
        st = time()
        func(*args, **kwargs)
        et = time()
        print(f"{func.__module__}.{func.__name__}: {et - st:6f}")

    return wrapper
