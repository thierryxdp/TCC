def filtra_pares(s):
    pares = tuple(it for it in s if it[1]//2 == 0)
    impares = tuple(it for it in s if it[1]//2 == 1)

    return pares