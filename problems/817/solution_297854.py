def acima_da_media(lista):
    
    i = len(lista)
    list.sort(lista)
    media = sum(lista)/i
    
    return lista[media:]