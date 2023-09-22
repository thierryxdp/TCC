def acima_da_media(lista, media):
    lista.append(lista, media)
    lista.sort()
    lista1=lista.index(lista, media)
    return lista[lista1+lista.count(lista, media):]