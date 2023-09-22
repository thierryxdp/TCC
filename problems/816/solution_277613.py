def maiores(lista,n):
    '''list,int->list'''
    lista1=lista+[n]
    list.sort(lista1)
    del lista1[:n]
    return lista1