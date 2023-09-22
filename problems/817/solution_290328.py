def acima_da_media(lista):
    media=sum(lista)/len(lista)
    mediaint=int(media)
    lista1=lista+[mediaint]
    list.sort(lista1)
    indice=list.index(lista1,mediaint)
    list.remove(lista1,mediaint)
    del lista1[0:indice+1]
    return lista1