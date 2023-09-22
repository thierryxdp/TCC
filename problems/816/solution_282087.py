def maiores(lista,n):
    lista1 = lista + [int(n)]
    lista2 = list.sort(lista1)
    lista3 = lista2[2:]
    return lista3