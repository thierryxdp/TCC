def filtra_pares(t):
    pares = []
    for i in t:
        if (i % 2  == 0):
            pares.append(i)
    return tuple(pares)