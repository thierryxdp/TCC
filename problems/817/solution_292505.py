def acima_da_media(lista):
    media_lista=sum(lista)/len(lista)
    list.append(lista,media_lista)
    list.sort(lista)
    indice=list.index(lista,media_lista)
    lista1=lista[indice:]
    lista2=lista[indice+2:]
    if media_lista not in lista:
        return lista1
    else:
        return lista2