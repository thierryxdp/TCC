def maiores(lista, n):
    ''''''
    lista = lista.sort()
    if lista > n:
        return lista
    else:
        return []