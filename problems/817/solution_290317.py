def acima_da_media(lista):
    media=sum(lista)/len(lista)
    media1=int(media)
    lista1=lista+[media1]
    list.sort(lista1)
    indice=list.index(lista1,media1)
    del lista1[0:indice+1]
    return lista1