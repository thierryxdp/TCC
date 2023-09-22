def acima_da_media(lista):
    media=(sum(lista))/(len(lista))
    lista=lista+[media]
    list.sort(lista)
    del lista[:(list.index(lista,(media+1)))]
    del lista[0]
    return lista