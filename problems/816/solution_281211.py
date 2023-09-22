def maiores(lista,n):
    lista=lista+[n]
    list.sort(lista)
    del lista[0:(list.index(lista,n))]
    return lista