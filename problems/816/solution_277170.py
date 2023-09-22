def maiores(lista,n):
    ''' '''
    if n not in lista:
        return lista
    elif n > lista: 
        lista=len(lista)
        lista=list()
        return lista