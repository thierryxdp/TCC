def maiores(lista,n):
    lista.insert(0,n)
    lista.sort()
    del lista[0:(lista.index(n)+1)]

    return lista