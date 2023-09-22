def acima_da_media (lista):
    b = lista[:]
    media = sum(lista) / len(lista)
    list.append(lista, media)
    list.sort(lista)
    a = list.index(lista, media)
    return b