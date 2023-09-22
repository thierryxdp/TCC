def acima_da_media(lista):
    media = round(sum(lista) / len(lista))
    if media not in lista:
        lista.insert(0,media)
        lista.sort()
        corte = lista.index(media)
        aprovados = lista[corte+1:]
        return aprovados
    lista.sort()
    corte = lista.index(media)
    aprovados = lista[-1:corte:-1]
    return aprovados