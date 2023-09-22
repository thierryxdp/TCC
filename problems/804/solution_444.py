def filtra_pares(tupla1):
    tupla2 = sorted(filter(lambda x: x % 2 == 0, tupla1))
    return tupla2