def filtra_pares(t):
    filtro = ()
    for n in t:
        if n%2 == 0:
        filtro = filtro + (n, )
    return filtro