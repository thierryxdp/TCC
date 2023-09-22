def maiores(lista,n):
    list.insert(lista,0,n)
    list.sort(lista)
    lista[list.index(lista,n):]
    del(lista,n)
    return lista