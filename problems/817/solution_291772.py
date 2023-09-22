def acima_da_media(lista):
    media=sum(lista)/len(lista)
    lista.append(media)
    lista.sort()
    lista=lista[lista.index(media)+1:]
    if media in lista:
        list.remove(lista,media)
        return lista
    else return lista