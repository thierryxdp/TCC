def acima_da_media(lista):
    media = sum(lista) / len(lista)
    list.append(lista,media)
    list.sort(lista)
    if (lista.count(media)<=1):
        x = lista[lista.index(media) + 1:]
        return x
    else:
        y = lista.index(media)
        del lista[lista.index(media)+1]
        return lista[y+1:]