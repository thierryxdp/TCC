def maiores(lista,n):
    list.sort(lista)
    a=list.index(n)
    del lista[:a]
    return lista