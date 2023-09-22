def maiores(lista,n):
    '''list,int->list'''
    lista1=lista+[n]
    list.sort(lista1)
    indice=list.index(lista1,n)
    del lista1[0:n]
    return lista1