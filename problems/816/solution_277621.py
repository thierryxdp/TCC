def maiores(lista,n):
    '''list,int->list'''
    lista1=lista+[n]
    list.sort(lista1)
    del lista1[0:[n+1]]
    return lista1