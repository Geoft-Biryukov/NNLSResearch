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