def maiores (J, n):
    list.sort(J)
    del J[:(n+1)]
    return J