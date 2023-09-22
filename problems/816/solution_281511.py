def maiores(lista,n):
    x = int(n)
    lista1 = lista + [x]
    lista2 = list.sort(lista1)
    lista3 = list.index(lista2,x)
    num = x-1
    lista4 = lista3[x:]
    return lista4