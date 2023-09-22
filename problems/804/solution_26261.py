def filtra_pares(x):
    pares = ()
    proximo = 0 
    while proximo < len(x):
        if t[proximo]%2 == 0:
            pares = pares + (t[proximo],)
            proximo = proximo + 1
            return pares