from scipy.optimize import nnls
import numpy as np

def matrix_to_str(a):    
    result = ''
    for i in range(0, a.shape[0]):
        for j in range(0, a.shape[1]):
            result += str(a[i, j]) + ' '
        result += '\n'
    return result

def vector_to_str(v):
    result = ''
    for i in range(0, v.shape[0]):        
        result += str(v[i]) + ' '        
    return '{ ' + result + '}'

A = np.array([[73, 71, 52], [87, 74, 46], [72, 2, 7], [80, 89, 871]])

print('A = ', matrix_to_str(A))

b = np.array([49, 67, 68, 20])

print('b = ', vector_to_str(b))

sol = nnls(A, b)

print('x = ', vector_to_str(sol[0]))