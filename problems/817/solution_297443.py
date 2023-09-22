def acima_da_media(lista):
    media=sum(lista)/len(lista)
    lista.append(media)
    lista.sort()
    posicao_media=lista.index(media)
    posicao_1dps_media=posicao_media+1

    if lista[posicao_media]==lista[posicao_1dps_media]:
        lista=lista[lista.index(media)+2:]
    else:
        lista=lista[lista.index(media)+1:]
    return lista