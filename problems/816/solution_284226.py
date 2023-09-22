def maiores(lista,n):
    lista.append(n)
    list.sort(lista)
    list.reverse(lista)
    a = list.index(lista,n)
    del lista[a:]
    list.reverse(lista)
    return lista