def acima_da_media(lista):
    media=sum(lista)/len(lista)
    if media == sum(lista):
        return []
    lista=lista+[media]
    lista.sort()
    lista=lista[(lista.index(media)+1):]
    return lista