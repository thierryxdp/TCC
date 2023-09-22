def acima_da_media(lista):
    media = sum(lista) / len(lista)
    list.append(lista,media)
    list.sort(lista)
    if (lista[lista.index(media)] != lista[lista.index(media)-1]):
        return lista[lista.index(media) + 1:]
    else:
        return lista