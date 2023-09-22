def maiores(lista,n):
    list.sort(lista,reverse=True)
    if n in lista:
        return list.reverse(lista[0,list.index(lista,n)])