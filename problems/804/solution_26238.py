def filtra_pares(tup):
    pares = ()
    i = 0
    while i < len(tup):
        if tup[i]%2 == 0:
            pares = pares + (tup[i],)
            i = i + 1
    return pares