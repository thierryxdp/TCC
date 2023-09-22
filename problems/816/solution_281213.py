def maiores(lista,n):
    lista=lista+[n]
    list.sort(lista)
    del lista[0:(list.index(lista,n))]
    list.insert(lista,0,n)
    return lista