def maiores (J, n):
    list.sort(J)
    e = list.index(n)
    del J[:(e+1)]
    return J