def filtra_pares(a):
    if not verifica(a):
        raise ValueError(’separa: argumento incorrecto.’)

    pares = tuple(it for it in a if it[0:]%2 = 0)
    impares = tuple(it for it in a if it[0:]%2 = 5)

    return (pares)