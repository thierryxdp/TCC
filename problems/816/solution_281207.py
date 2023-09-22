def maiores(lista,n):
    list.sort(lista)
    del (lista+[n])[0:(index(n))]
    return lista