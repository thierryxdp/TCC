def maiores(lista,n):
    list.sort(lista)
    del (lista+[n])[0:(list.index(n))]
    return lista