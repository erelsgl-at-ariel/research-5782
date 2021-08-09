#import integrate as pyint
#import c_integrate as c_int
import timeit

cy = timeit.timeit('c_integrate.integrate(20,30,100)',
                    setup='import c_integrate',
                    number = 100000 )

py = timeit.timeit('integrate.integrate(20,30,100)',
                    setup='import integrate',
                    number = 100000 )

print(f'cy = {cy}')
print(f'py = {py}')
print(f'Cython is {py/cy}x faster')
