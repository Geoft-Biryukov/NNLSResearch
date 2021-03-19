import numpy as np


def get_vectors_from_file(file_name, sep=' '):
    result = []
    with open(file_name, 'r') as f:
        for line in f:
            arr = np.fromstring(line, sep=sep)
            result.append(arr)
    return result


def get_matrix_from_file(file_name):
    rows = get_vectors_from_file(file_name, ',')
    n = len(rows)
    cols_len = []
    for row in rows:
        cols_len.append(len(row))
    m = cols_len[0]
    for k in cols_len:
        if k != m:
            raise RuntimeError('columns count mismatch')

    result = np.empty([n, m])
    i = 0
    for row in rows:
        result[i] = row
        i = i + 1

    return result
