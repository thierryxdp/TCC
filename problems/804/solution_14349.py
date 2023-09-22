def filtra_pares(t):
    pares = list(filter(lambda x: x % 2 == 0, t))
    pares=tupla(pares)
    return pares