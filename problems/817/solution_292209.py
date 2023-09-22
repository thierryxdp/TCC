def acima_da_media(lista):
    media = sum(lista) / len(lista)
    list.append(lista,media)
    list.sort(lista)
    if (str.count(lista,media)<1):
        x = lista[lista.index(media) + 1:]
        return x