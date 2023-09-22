def acima_da_media(lista):
    media = [sum(lista)//len(lista)]
    lista = lista + [media]
    lista = lista.sort()
    indice = lista.index(media)
    del (lista[0:media])
    return lista