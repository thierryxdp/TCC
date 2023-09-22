def acima_da_media(lista):
    
    i = len(lista)
    media = sum(lista)/i
    media_total = list.index(lista,media)
    
    return lista[media_total:]