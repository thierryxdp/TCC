def maiores(lista, n):
    """"""
    list.sort(lista)
    if n>max(lista):
        return []
    elif n+1 in lista:
        return lista[list.index(lista, n+1):]
    elif n-1 in lista:
        return lista[list.index(lista, n-1):]
    elif n<min(lista):
        return lista