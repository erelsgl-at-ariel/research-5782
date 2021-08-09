from libc.math cimport sin

cdef f(x):
    return sin(x**2)

cpdef double integrate(double a,double b,int N):
    cdef double s = 0
    cdef double dx = (b-a)/N
    cdef int i
    for i in range(N):
        s+= f(a+i*dx)
    return s * dx