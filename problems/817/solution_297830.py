def acima_da_media(lista):
    
    i = len(lista)
    list.sort(lista)
    
    acima_media = list.index(lista,7.0)
    
    return lista[acima_media]