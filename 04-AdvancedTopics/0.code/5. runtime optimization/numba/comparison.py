from numba import njit , vectorize, int32, int64
from functools import wraps
import time

def my_timer(orig_func):
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{ orig_func.__name__} ran in: { t2} sec')
        return result
    return wrapper

@my_timer
def f(x_range,y_range,z_range):
    lst = []
    for x in range(x_range):
        for y in range(y_range):
            for z in range(z_range):
                if (z + x + y)/10 == x:
                    lst.append(x)
    return lst

@my_timer
@njit
def njit_f(x_range,y_range,z_range):
    lst = []
    for x in range(x_range):
        for y in range(y_range):
            for z in range(z_range):
                if (z + x + y)/10 == x:
                    lst.append(x)
    return lst



x_range = 10
y_range = 10
z_range = 10
print(f'x = {x_range} , y = {y_range} , z= {z_range}')
f(x_range,y_range,z_range)
njit_f(x_range,y_range,z_range)

y_range = 1000
z_range = 1000
print(f'\nx = {x_range} , y = {y_range} , z= {z_range}')
f(x_range,y_range,z_range)
njit_f(x_range,y_range,z_range)

z_range = 10000
print(f'\nx = {x_range} , y = {y_range} , z= {z_range}')
f(x_range,y_range,z_range)
njit_f(x_range,y_range,z_range)


