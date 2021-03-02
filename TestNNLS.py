from scipy.optimize import nnls
import numpy as np

from ToStrConverters import *
from  TestMatrixGenerators import *

print('Example 1')
(A, b, res) = CreateLeastSquareProblemBro()
sol = nnls(A, b)

print('A =\n', matrix_to_str(A))
print('b = ', vector_to_str(b))
print('x = ', vector_to_str(sol[0]))
print('expected = ', vector_to_str(res))

print('\n')
print('*****************************************')
print('\n')

print('Example 2')
(A, b, res) = CreateLeastSquareProblemHansen()
sol = nnls(A, b)

print('A =\n', matrix_to_str(A))
print('b = ', vector_to_str(b))
print('x = ', vector_to_str(sol[0]))
print('expected = ', vector_to_str(res))
