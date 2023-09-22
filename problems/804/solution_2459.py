def filtra_pares(tupla):
    pares = sorted(filter(lambda x: x % 2 == 0, tupla))
    return (pares)