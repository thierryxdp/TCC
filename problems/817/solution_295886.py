def acima_da_media(lista):
    media=(sum(lista))/(len(lista))
    lista=lista+[media]
    list.sort(lista)
    del lista[0:(list.index(lista,media))]
    return lista