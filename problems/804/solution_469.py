def filtra_pares(tupla1):
    tupla2 = (list(filter(lambda x: x % 2 == 0, tupla1)))
    return str(tupla2)