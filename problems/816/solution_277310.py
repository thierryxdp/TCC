def maiores(lista,n):
    ''' '''
    if n not in lista:
        return lista
    elif n in lista: 
        lista=n < lista
        lista=len(lista)
        lista=list.sort(lista)
        return lista