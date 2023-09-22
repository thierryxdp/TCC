def maiores(lista,n):
    lista.append(n)
    list.sort(lista)
    x=lista.index(n)
    del(lista[:n-1])
    return lista