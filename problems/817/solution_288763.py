def acima_da_media(lista):
    media=sum(lista)//len(lista)
    lista.sort()
    return lista[lista.index(media)+1:]