def maiores(lista,n):
    lista1 = lista + [int(n)]
    list.sort(lista1)
    k = list.index(lista1,int(n))
    lista3 = lista1[k+1:]
    return lista3