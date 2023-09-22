def maiores(lista, n):
    list.insert(lista,0, n)
    list.sort(lista)
    i=list.index(lista, n)
    return lista[i:]