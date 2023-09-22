def maiores (lista,n):
    list.sort(lista)
    p = list.index(lista,n)
    x = lista[p:]
    return x