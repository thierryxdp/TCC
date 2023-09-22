def maiores(lista,n):
    lista.insert(1,n)
    lista.sort()
    sublist = lista.index(n)
    return lista[sublist+1:]