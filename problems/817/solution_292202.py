def acima_da_media(lista):
    media = sum(lista) / len(lista)
    list.append(lista,media)
    list.sort(lista)
    x = lista[lista.index(media) + 1:]
    x[0] = int(media)
    return x