def maiores(lista,n):
    list.sort(lista)
    a=list.index(lista,n)
    del lista[:a]
    return lista