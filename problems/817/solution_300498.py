def acima_da_media(lista):
    ''
    soma = sum(lista)
    media = (soma)/len(lista)
    lista = lista + [media]
    list.sort(lista)
    p = lista.index(media)
    lista = lista[p:]
    list.remove(lista,media)
    if media == lista[0]:
        return []
    else:
        return lista