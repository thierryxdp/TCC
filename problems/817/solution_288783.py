def acima_da_media(lista):
    lista.sort()
    media=sum(lista)//len(lista)
    if lista.index(media)>-1:
        return lista[lista.index(media)+1:]
    elif media not in lista:
        lista2=lista+[media]
        lista2.sort()
        return lista2[lista2.index(media)+1:]