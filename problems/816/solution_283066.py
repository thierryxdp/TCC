def maiores(lista_numero,n):
    lista=lista_numero+[n]
    list.sort(lista)
    x=list.index(lista,n)
    del lista[:x-1]
    list.sort (lista)
    return lista