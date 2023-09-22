def filtra_pares(x, y, z, w):
    tuple = x, y, z, w
    lista1 = [x, y, z, w]
    lista2 = filter(lambda x: x % 2 == 0, lista1)
    return lista2