def maiores(lista,n):
    list.insert(n,lista,-1)
    list.sort(lista)
    del lista[:n]

    return lista