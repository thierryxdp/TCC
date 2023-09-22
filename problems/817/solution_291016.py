def acima_da_media(lista):
    if media not in lista:
    media=sum(lista)/len(lista)
    lista.append(media)
    lista.sort()
    lista=lista[lista.index(media)+1:]
    else:
        media=sum(lista)/len(lista)
    lista.append(media)
    lista.sort()
    list.remove(lista,media)
    lista=lista[lista.index(media)+1:]
    return lista