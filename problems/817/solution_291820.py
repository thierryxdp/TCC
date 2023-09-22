def acima_da_media(lista):
    ''' '''
    media = sum(lista) / len(lista)
    
    list.sort(lista)
    indice = list.index(lista,media)
    lista = lista[:indice:-1]
    list.reverse(lista)
    return lista