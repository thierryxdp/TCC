def filtra_pares(x):
    '''.'''
    a = x[0]
    b = x[1]
    c = x[2]
    d = x[3]
    pares = filter(lambda x: x % 2 == 0, x)
    pares = tuple(pares)
    return pares