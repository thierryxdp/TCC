def maiores(lista,n):
    lista1=lista+[n]
    list.sort(lista1)
    lista2 = lista1[list.index(lista,n) +1:]
    return lista2