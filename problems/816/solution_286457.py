def maiores(lista,n):
    ''' '''
    #h= lista
    #num=[n]
    
    if lista[0:] < n:
        lista = list.sort(lista)
    else:
        lista = []
    return lista