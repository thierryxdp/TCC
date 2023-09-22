def maiores(lista,n):
    str.sort(lista)
    str.insert(n,lista)
    del lista[:n]

    return lista