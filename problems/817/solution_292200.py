def acima_da_media(lista):
    media = sum(lista) / len(lista)
    list.append(lista,media)
    list.sort(lista)
    if (lista[lista.index(media)] != int):
        return lista[lista.index(media) + 1:]
    else: