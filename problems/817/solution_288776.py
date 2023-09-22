def acima_da_media(lista):
    media=sum(lista)//len(lista)
    lista2=[media]
    if lista.index(media)>-1:
        return lista[lista.index(media)+1:]