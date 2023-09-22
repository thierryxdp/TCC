def maiores(lista,n):
    ''' '''
    if n not in lista:
        return lista
    else:
        return (list.sort(lista,n)(list.index(lista,n)))