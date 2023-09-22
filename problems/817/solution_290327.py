def acima_da_media(lista):
    media=sum(lista)/len(lista)
    lista1=lista+[media]
    list.sort(lista1)
    indice=list.index(lista1,media)
    mediaint=int(media)
    if mediaint in lista1:
        del lista1[indice]
    del lista1[0:indice]
    return lista1