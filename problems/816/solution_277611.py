def maiores(lista,n):
    '''list,int->list'''
    lista1=lista+[n]
    list.sort(lista1)
    list.remove(lista1,lista1[0:n])
    return lista1