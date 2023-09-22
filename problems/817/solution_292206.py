def acima_da_media(lista):
    media = sum(lista) / len(lista)
    list.append(lista,media)
    list.sort(lista)
    if ( media > lista[lista.index(media)]):
        x = lista[lista.index(media) + 1:]
        return x
    else:
        del lista