def filtra_pares(t):
    pares = ()
    proximo = 0
    while proximo <len(t):
        if t[proximo]%2 == 0:
            pares = pares + (t[proximo],)
        proximo = proximo + 1
    return pares