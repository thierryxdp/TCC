def acima_da_media(lista):
    media=sum(lista)/len(lista)
    lista1=lista+[int(media)]
    list.sort(lista1)
    indice=list.index(lista1,media)
    del lista1[0:indice+1]
    return lista1