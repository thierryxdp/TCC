def maiores (lista,n):
    list.append(lista,n)
    list.sort(lista)
    p = list.index(lista,n)
    x = lista[p:]
    del x[0]
    return x