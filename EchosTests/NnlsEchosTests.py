import os

import numpy as np
from scipy.optimize import nnls

from lsqgen import *

current_path = os.path.dirname(os.path.realpath(__file__))

echos_file = os.path.join(current_path, 'test_echos.mtr')
kernel_file = os.path.join(current_path, 'test_matrix.mtr')
solution_file = os.path.join(current_path, 'test_solutions.mtr')

echos = get_vectors_from_file(echos_file)
kernel = get_matrix_from_file(kernel_file)
ext_sols = get_vectors_from_file(solution_file)

echos_len = len(echos)
if echos_len != len(ext_sols):
    raise RuntimeError('len(echos) != len(ext_sols)')

sol = []
counter = 1
for echo in echos:
    sol.append(nnls(kernel, echo))
    if counter % 10 == 0:
        print('Completed ', counter, ' of ', echos_len)
    counter += 1

print('Process is completed ', counter - 1, ' of ', echos_len)

i = 0
tol_flag = True
index_of_wrong_solution = -1
for i in range(len(echos)):
    if not np.allclose(ext_sols[i], sol[i][0], atol=1e-10):
        tol_flag = False
        index_of_wrong_solution = i
        break

if tol_flag:
    print('All solutions within tolerance')
else:
    print('Wrong solution: index = ', index_of_wrong_solution)

print("Hello")

input()
