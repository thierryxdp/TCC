def diltra_pares(tupla):
    lista1 = tupla
    lista2 = sorted(filter(lambda x: x % 2 == 0, lista1))
    return lista2