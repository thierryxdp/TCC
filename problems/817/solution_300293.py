def acima_da_media(lista):
    media = sum(lista)//len(lista)
    lista.append(media)
    listaOrganizada = sorted(lista)
    mediaIndice = listaOrganizada.index(media)
    listaN = listaOrganizada[mediaIndice + 1:].copy()

    if media in listaN:
        del listaN[0]

    return listaN