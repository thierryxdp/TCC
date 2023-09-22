def maiores(lista,n):
    list.sort(lista)
    del lista[:n-5]
    return lista