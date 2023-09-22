def filtra_pares(t):
    l = list()
    for k in t if (k % 2 == 0):
        l.append(k)
        return tuple(l)