def filtra_pares(tup):
    pares = ()
    i = 0
    while i < len(tup):
        if tup[i]%2 ==0:
        pares = pares + (tup[i],)
        contador = contador + 1
    return pares