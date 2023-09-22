def acima_da_media(lista):
    media=sum(lista)//len(lista)
    lista2=[media]
    lista2=lista+lista2
    lista2.sort()
    return lista2[lista2.index(media)+1:]