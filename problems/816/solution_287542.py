def maiores(lista,n):
    list.sort(lista)
    list.insert(n,lista)
    del lista[:n]

    return lista