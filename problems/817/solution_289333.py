def acima_da_media(lista, media):
    lista.append(media)
    lista.sort()
    lista1=lista.index(media)
    return lista[lista1+lista.count(media):]