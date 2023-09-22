def acima_da_media(lista):
    numero_elem=len(lista)
    media=sum(lista)//numero_elem
    list.sort(lista)
    if media in lista==True :
        return lista[lista.index(media)+1]
    elif media not in lista==True:
        lista2=lista+[media]
        lisa2.sort()
        return lista2[lista2.index(media)+1]