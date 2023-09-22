def acima_da_media(lista):
    media = [sum(lista)//len(lista)]
    lista = lista + [media]
    lista1 = list.sorted(lista)
    indice = lista.index(media)
    del (lista[0:media])
    return lista