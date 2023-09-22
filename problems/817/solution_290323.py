def acima_da_media(lista):
    media=sum(lista)/len(lista)
    lista1=lista+[media]
    list.sort(lista1)
    indice=list.index(lista1,media)
    if int(media) in lista 1:
        del lista1[indice]
    del lista1[0:indice+1]
    return lista1