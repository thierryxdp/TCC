def acima_da_media(lista):
    media=sum(lista)/len(lista)
    list.sort(lista)
    lista1=lista+[media]
    indice=list.index(lista1,media)
    del lista1[0:indice+1]
    return lista1