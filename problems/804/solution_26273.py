def filtra_pares(x):
    pares =()
    proximo = 0
    while proximo < len(x):
        if x[proximo]%2 == 0:
            pares = (x[proximo],)
            return pares