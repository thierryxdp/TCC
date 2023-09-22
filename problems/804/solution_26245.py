def filtra_pares(tup):
    pares = filter(lambda valor: valor %2 == 0, tup)
    return tuple(pares)