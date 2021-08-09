cpdef int test(int x):
    cdef int y=0
    cdef int i = 0
    for i in range(x):
        y+=i
    return y