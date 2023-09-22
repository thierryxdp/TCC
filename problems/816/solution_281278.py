def maiores(lista, n):
    list.insert(lista,0, n)
    list.sort(lista)
    a = list.index(lista, n)
    return lista[-1:a]