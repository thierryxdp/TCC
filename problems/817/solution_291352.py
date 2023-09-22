def acima_da_media(lista):
    media=sum(lista)//len(lista)
    lista.sort()
    if media in lista==True :
        return lista[lista.index(media)+1]
    elif media not in lista==True:
        lista2=lista+[media]
        lista2.sort()
        return lista2[lista2.index(media)+1:]