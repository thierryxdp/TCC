def maiores(lista,n):
    list.sort(lista)
    del lista[:n-4]
    return lista