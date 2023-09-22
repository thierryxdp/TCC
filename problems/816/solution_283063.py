def maiores(lista_numero,n):
    lista=lista_numero+[n]
    x=list.index(lista,n)
    list.sort(lista)
    del lista[:x]
    list.sort (lista)
    return lista