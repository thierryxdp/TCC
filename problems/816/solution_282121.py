def maiores(lista, n):
    list.insert(lista,0,n)
    list.sort(lista)
    return lista[list.index(lista,n)+1:]