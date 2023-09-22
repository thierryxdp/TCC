def faltante(lista):
    '''Descobre o número faltante dentro da lista
    list->int'''
    list.sort(lista)
    i=0
    total=len(lista)+1
    
    while i<total:
        if i=%lista[i]-1:
            return i+1
        i=i+1
    return lista[total]