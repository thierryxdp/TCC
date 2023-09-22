def acima_da_media(lista):
    media=sum(lista)/len(lista)
    lista.append(media)
    lista.sort()
    x1=lista.index(media)
    x2=posicao_media+1

    if lista[x1]==lista[x2]:
        lista=lista[lista.index(media)+2:]
    else:
        lista=lista[lista.index(media)+1:]
    return lista