def filtra_pares(x):
    '''.'''
    a = x[0]
    b = x[1]
    c = x[2]
    d = x[3]
    result = filter(lambda x: x % 2 == 0, x)
    result = tuple(result)
    return result