def maiores(lista,n):
    lista=sorted(lista)
    del lista[::n]
    return lista