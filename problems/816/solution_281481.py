def maiores(lista,n):
    list.sort(lista)
    list.index(lista,n)
    del lista[:n]
    return lista