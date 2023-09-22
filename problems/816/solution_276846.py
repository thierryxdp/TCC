def maiores(lista,n):
    list.sort(lista)
    for c in lista:
        if n>c:
            return lista[list.index(lista,c):]
        if n<c:
            return lista