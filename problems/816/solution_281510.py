def maiores(lista,n):
    lista1 = lista + [int(n)]
    lista2 = list.sort(lista1)
    lista3 = list.index(lista2,int(n))
    lista4 = lista3[(int(n) - 1):]
    return lista4