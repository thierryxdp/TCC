def filtra_pares([x, y, z, w]):
    tuple = x, y, z, w
    lista1 = [4, 3, 2, 5, 7, 6]
    lista2 = filter(lambda x: x % 2 == 0, lista1)
    return lista2