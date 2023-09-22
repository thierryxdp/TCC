def maiores(lista,n):
    lista += [n]
    list.sort(lista)
    del lista[:n-1]
    return lista