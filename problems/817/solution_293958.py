def acima_da_media (lista):
    media = sum(lista) / len(lista)
    list.append(lista, media)
    list.sort(lista)
    a = list.index(lista, media)
    if media not in lista and int(media) in lista:
        return lista[a+2:]
    elif media not in lista:
        return lista[a+1:]