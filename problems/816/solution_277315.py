def maiores(lista,n):
    ''' '''
    if n not in lista:
        return lista
    elif n in lista: 
        lista=n < lista
        lista=list.sorted(lista)
        return lista