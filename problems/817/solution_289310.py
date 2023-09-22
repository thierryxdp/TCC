def acima_da_media(lista):
    list.sort(lista)
    media = sum(lista)//len(lista)
    if media in lista:
        return lista[list.index(lista, media)+1:]
    else:
        return lista[len(lista)//2:]