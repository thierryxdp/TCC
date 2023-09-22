def maiores(lista, n):
    '''
    '''
    list.insert(lista,1,n)
    list.sort(lista)
    indice = list.index(lista,n)
    return lista[indice:]