def acima_da_media(lista):
    
    media = sum(lista)/len(lista)
    list.sort(lista)
    return [lista.index(media)+1:]