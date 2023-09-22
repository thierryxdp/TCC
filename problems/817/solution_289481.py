def acima_da_media(lista):
    media = sum(lista)/len(lista)
    list.append(media)
    list.sort(lista)
    posicao_media = list.index(lista, media)
    return lista[posicao_media+1:]