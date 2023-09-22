def acima_da_media(lista):

    media = sum(lista)/len(lista)

    list.sort(lista)

    lista_nova = lista[int(media):]

    return lista_nova