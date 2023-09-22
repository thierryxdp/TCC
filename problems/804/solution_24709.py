def filtra_pares(naturais):
    pares = []
    for i in naturais:
        if i % 2 == 0:
            pares.append(i)
    
    return tuple(pares)