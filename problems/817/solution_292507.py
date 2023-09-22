def acima_da_media(lista):
    media_lista=sum(lista)/len(lista)
    list.append(lista,media_lista)
    list.sort(lista)
    indice=list.index(lista,media_lista)
    lista1=lista[indice+1:]
    return lista1