def acima_da_media(lista):
    lista.sort()
    media=sum(lista)//len(lista)
    lista2=[media]
    if lista.index(media)>-1:
        return lista[lista.index(media)+1:]
    else:
        lista2=lista+lista2
        lista2.sort()
        return lista2[lista.index(media)+1:]