def acima_da_media(lista):
    media=sum(lista)/len(lista)
    lista=lista+[media]
    lista=lista[(lista.index(media)+1):]
    return lista