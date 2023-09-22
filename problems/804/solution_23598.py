def filtra_pares(a,b,c,d):
    f = [a,b,c,d]
    for i in range 3:
        if f[i]%2 == 0:
            return tuple(f[i])