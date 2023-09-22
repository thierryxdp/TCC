def acima_da_media (lista1):
    '''retorna uma lista com as notas maiores que a media da lista1
    list->list'''
    
    if len(lista1)==1:
        return []
    else:
    n = (sum(lista1)/len(lista1))
    list.append(lista1,n)
    list.sort(lista1)
    a=list.index(lista1,n)
    del lista1[0:(a+1)]
    return lista1