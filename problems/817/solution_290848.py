def acima_da_media(lista):
    media = round(sum(lista) / len(lista))
    lista.insert(0,media)
    lista.sort()
    corte = lista.index(media)
    aprovados = lista[corte:]
    return aprovados