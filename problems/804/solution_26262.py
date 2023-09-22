def filtra_pares(x):
    pares = ()
    proximo = 0 
    while proximo < len(x):
        if x[proximo]%2 == 0:
            pares = pares + (x[proximo],)
            proximo = proximo + 1
            return pares