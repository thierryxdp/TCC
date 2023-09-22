def maiores(lista,n):
    list.sort(lista)
    x=list.index(lista,n)
    del lista[:x]
    return lista