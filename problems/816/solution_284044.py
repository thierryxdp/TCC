def maiores(lista, n):
    lista = list.insert(lista, 1, n)
    return lista == list.insert(lista, 1, n)