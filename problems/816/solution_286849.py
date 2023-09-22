def maiores(lista, n):
    if n not in lista:
        list.append(lista,n)
    list.sort(lista)
    i = list.index(lista,n)
    return lista[i+1:]