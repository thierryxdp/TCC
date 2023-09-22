def filtra_pares(lista1):
    lista2 = filter(lambda x: x % 2 == 0, lista1)
    return str(lista2)