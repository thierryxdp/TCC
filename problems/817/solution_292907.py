def acima_da_media(lista):
    media = sum(lista) / len(lista)
    lista.append(media)
    lista.sort()
    if lista[lista.index(media)] == lista[lista.index(media)+1]:
        return lista[lista.index(media)+2:]
    else:
        return lista[lista.index(media)+1:]