def maiores(lista,n):
    ''' '''
    if n not in lista:
        return sorted(lista)
    elif n in lista:
        return lista>n
    else: 
        return sorted(lista)