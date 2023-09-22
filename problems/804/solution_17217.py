def filtra_pares(t):
    pares = ()
    for proximo in t:
        if proximo%2 == 0:
            pares = pares + (proximo,)
    return pares