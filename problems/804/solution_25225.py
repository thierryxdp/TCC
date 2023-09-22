def filtra_pares(tup):
    pares = []
    for n in tup:
        if n%2==0:
            pares.append(n)
    return pares