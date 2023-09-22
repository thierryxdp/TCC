def maiores(lista_int,n):
    list.append(lista_int,n)
    list.sort(lista_int,n)
    m = list.index(lista_int,n)
    maiores = lista_int[m+1:]
    return maiores