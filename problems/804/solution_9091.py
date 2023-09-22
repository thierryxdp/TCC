def filtra_pares(t):
    copia=()
    for x in t:
        if x%2==0:
            copia= copia+tuple(x)
        else:
            pass
    return copia