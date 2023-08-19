'''Написати декоратор, котрий задекорує функцію і порахує час виконання самої функції.'''


import time
def calc_time(func):
    def wrapper(*args):
        start_time = time.time()
        res = func(*args)
        finish_time = time.time()
        duration = finish_time - start_time
        print(duration)
        return res
    return wrapper

@calc_time
def example_func(*args):
    for i in range(*args):
        print(i ** 2)

example_func(100000)