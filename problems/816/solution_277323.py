def maiores(lista,n):
    ''' '''
    if n not in lista:
        return lista
    elif n in lista: 
        lista=list.sorted(lista)
        return lista