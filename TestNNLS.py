from scipy.optimize import nnls
import numpy as np

from ToStrConverters import *

A = np.array([[73, 71, 52], [87, 74, 46], [72, 2, 7], [80, 89, 871]])

print('A = ', matrix_to_str(A))

b = np.array([49, 67, 68, 20])

print('b = ', vector_to_str(b))

sol = nnls(A, b)

print('x = ', vector_to_str(sol[0]))
