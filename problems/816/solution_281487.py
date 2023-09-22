def maiores(lista,n):
    list.sort(lista)
    del lista[:n-8]
    return lista