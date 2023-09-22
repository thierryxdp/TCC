def filtra_pares(t):
    pares = list(filter(lambda x: x % 2 == 0, t))
    pares=tuple(pares)
    return pares