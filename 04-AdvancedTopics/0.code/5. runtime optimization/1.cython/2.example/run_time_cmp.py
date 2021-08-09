
import timeit

cy = timeit.timeit('cy_example.test(500)',
                    setup='import cy_example',
                    number = 10000 )

py = timeit.timeit('py_example.test(500)',
                    setup='import py_example',
                    number = 10000 )

print(f'cy = {cy}')
print(f'py = {py}')
print(f'Cython is {py/cy}x faster')
