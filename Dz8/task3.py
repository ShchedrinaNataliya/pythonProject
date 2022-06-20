from functools import wraps

def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        numbers_list = [el for el in (*args, *kwargs.values())]
        n = [f"{func.__name__}({el}: {type(el)})" for el in numbers_list]
        print(*n, *func(*args, **kwargs), sep=",\n")
    return wrapper

@type_logger
def val_cube(*x, **y):
    numbers_list = [el for el in (*x, *y.values()) if isinstance(el, int) or isinstance(el, float)]
    return [i ** 3 for i in numbers_list]

a = val_cube(3, 54, 7.4, 5/6, 6.59)