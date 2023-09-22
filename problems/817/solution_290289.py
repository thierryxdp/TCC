def acima_da_media(lista):
    media = sum(lista)//len(lista)
    list.insert(lista, media, 0)
    list.sort(lista)
    return media