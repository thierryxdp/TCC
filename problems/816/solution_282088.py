def maiores(lista,n):
    lista1 = lista + [int(n)]
    lista1 = list.sort(lista1)
    lista3 = lista1[2:]
    return lista3