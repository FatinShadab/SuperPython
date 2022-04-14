from loop import income_sum_loop
from taxes import tax_python
import numpy as np
import timeit

incomes = ([i for i in range(5000, 10000)]+[i for i in range(80000, 10000000)])

start_time = timeit.default_timer()
sum((tax_python(i) for i in incomes))
runtime_py = timeit.default_timer()-start_time
print(f"Without cython: {runtime_py}")
income_sum_loop(np.array(incomes))
start_time = timeit.default_timer()

runtime_cy = timeit.default_timer()-start_time
print(f"With cython: {runtime_cy}")

print(f"Python is {runtime_py/runtime_cy}x slower")