def maiores(lista,n):
    if n not in lista:
        list.append(lista,n)
        list.sort(lista)
        list.index(lista,n)
    else:
        list.sort(lista)
        list.index(lista,n)
    return lista[list.index(lista,n)+1:]