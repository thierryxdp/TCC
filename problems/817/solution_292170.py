def acima_da_media(lista):
    media = sum(lista) / len(lista)
    if (lista[lista.index(media)] != lista[lista.index(media)-1]):
        list.append(lista,media)
        list.sort(lista)
        return lista[lista.index(media) + 1:]
    else:
        list.append(lista, int(media))
        list.sort(lista)
        return lista[lista.index(int(media))+1:]