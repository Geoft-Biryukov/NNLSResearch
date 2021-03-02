def matrix_to_str(a):    
    result = ''
    for item in a:        
        result += ''.join(str(e) + ' ' for e in item) + '\n'        
    return result

def vector_to_str(v):
    result = ''.join(str(e) + ' ' for e in v)            
    return '{ ' + result + '}'