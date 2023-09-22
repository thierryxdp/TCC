def maiores(lista,n):
    ''' '''
    if n not in lista:
        return lista
    elif n > len(lista): 
        lista=list()
        return lista