#import integrate as pyint
#import c_integrate as c_int
import timeit

cy = timeit.timeit('integrate(20,30,10000)',
                    setup='from cy_integrate import integrate',
                    number = 1000 )

py = timeit.timeit('integrate(20,30,10000)',
                    setup='from py_integrate import integrate',
                    number = 1000 )

print(f'cy = {cy}')
print(f'py = {py}')
print(f'Cython is {py/cy} times faster')
