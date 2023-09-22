def acima_da_media(lista):
    (list.sum(lista))/(len(lista))=media
    lista=lista+[media]
    list.sort(lista)
    del lista[0:(list.index(lista,media))]
    del lista[0]
    return lista