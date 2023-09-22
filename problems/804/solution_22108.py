def filtra_pares(t):
    l = list()
    l.append(k for k in t if k%2==0)
    return tuple(l)