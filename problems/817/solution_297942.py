def acima_da_media(lista):
    '''...'''
    
    lista1 = sum(lista)
    lista2 = len(lista)
    lista3 = lista1/lista2
    
    list = lista
    list.append(lista3)
    list.sort()
    list = list[(list.index(lista3)+1):]
    
    return lista3