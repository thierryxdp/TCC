def acima_da_media(lista):
    media = int(sum(lista) / len(lista))
    if media in lista:
        lista.sort()
        corte = lista.index(media)
        aprovados = lista[corte+1:]
        return aprovados
    lista.insert(0,media)
    lista.sort()
    corte = lista.index(media)
    aprovados = lista[corte+1:]
    return aprovados