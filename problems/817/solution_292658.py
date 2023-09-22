def acima_da_media(lista):
    media = sum(lista) / len(lista)
    list.sort(lista)
    while len(lista) > 0 and lista[0] < media:
        del lista[0]
    return lista