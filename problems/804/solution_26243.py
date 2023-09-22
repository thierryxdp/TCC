def filtra_pares(t):
    pares = ()
    i = 0
    while i < len(t):
        t[i]%2 == 0:
        pares = pares + (t[i],)
        i = i + 1
    return pares