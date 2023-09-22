def maiores(lista,n):
    list.sort(lista,reverse=True)
    list.reverse(lista[0,list.index(lista,n)])
    if n in lista:
        return lista