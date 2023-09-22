def maiores(lista, n):
    list.insert(lista,0, n)
    list.sort(lista)
    a = list.index(lista, n)
    b = a-1
    return lista[b:-1]