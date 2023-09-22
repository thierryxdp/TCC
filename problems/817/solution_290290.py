def acima_da_media(lista):
    media = sum(lista)//len(lista)
    list.insert(lista, 0, media)
    list.sort(lista)
    return lista[media:]