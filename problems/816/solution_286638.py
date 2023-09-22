def maiores(lista,n):
    list.sort(lista)
    if n in lista:
        del lista(0:list.index(lista,n))
    return lista