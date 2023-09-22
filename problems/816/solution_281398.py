def maiores(lista,n):
    lista=sorted(lista)
    del lista[0::n]
    return lista