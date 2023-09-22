def acima_da_media(lista):
    
    i = len(lista)
    list.sort(lista)
    algarismo = list.index(lista,7)
    
    return lista[:algarismo]