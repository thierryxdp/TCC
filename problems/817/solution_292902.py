def acima_da_media(lista):
    media = sum(lista) / len(lista)
    lista.append(media)
    lista.sort()
    return lista[lista.index(media):]