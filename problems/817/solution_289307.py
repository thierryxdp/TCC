def acima_da_media(lista):
    list.sort(lista)
    media = sum(lista)//len(lista)
    return lista[list.index(lista, media):]