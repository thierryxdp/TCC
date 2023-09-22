def maiores (J, n):
    list.sort(J)
    e = list.index(J, n)
    del J[:(e+1)]
    return J