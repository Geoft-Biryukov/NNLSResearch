import numpy as np
from scipy.optimize import nnls

from lsqgen import *

echos_file = 'd:\\Projects\\Python\\NNLSResearch\\EchosTests\\test_echos.mtr'
kernel_file = 'd:\\Projects\\Python\\NNLSResearch\\EchosTests\\test_matrix.mtr'
solution_file = 'd:\\Projects\\Python\\NNLSResearch\\EchosTests\\test_solutions.mtr'

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
    print('Completed ', counter, ' of ', echos_len)
    counter += 1

i = 0
for i in range(len(echos)):
    if np.allclose(ext_sols[i], sol[i][0], atol = 1e-10) :
        print("All right")
    else:
        print('Very bad!!!')
        raise RuntimeError('Very bad!!!')

input()