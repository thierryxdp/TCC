def acima_da_media (lista):
    a = lista
    media = sum(lista) / len(lista)
    list.append(lista, media)
    list.sort(lista)
    a = list.index(lista, media)
    return a