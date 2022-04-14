import cython
from taxesC import tax_cython

cpdef double income_sum_loop(long[:] incomes):
    cdef int i
    cdef int n = incomes.shape[0]
    cdef double tot = 0
    for i in range(n):
        tot += tax_cython(incomes[i])
    return tot