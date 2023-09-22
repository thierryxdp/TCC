def maiores(lista,n):
    if (n in lista)==True:
        return lista[:(list.index(lista,n)-1)]
    else:
        list.sort(lista)
        if n<lista[0]:
            return lista