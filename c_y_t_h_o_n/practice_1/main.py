from primeNum import prime_finder_vanilla
from primeNumC import prime_finder_optimized
import time

start_py = time.time()
prime_finder_vanilla(10000)
end_py = time.time()-start_py
print(f"Without cython: {end_py}")
start_cy = time.time()
prime_finder_optimized(10000)
end_cy = time.time()-start_cy
print(f"With Cython: {end_cy}")
print(f"Def {(end_py/end_cy)}")