def maiores(lista,n):
    if (n in lista)==True:
        return lista[:(list.index(lista,n)-1)]
    else:
        sort=[:]
        list.sort(sort)
        if n<sort[0]:
            return lista