def acima_da_media (lista):
    media = sum(lista) / len(lista)
    list.append(lista, media)
    list.sort(lista)
    a = list.index(lista, media)
    if media not in lista:
        return lista[a+1:]
    elif media in lista:
        return lista[a+2:]