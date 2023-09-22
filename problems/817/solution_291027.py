def acima_da_media(lista):
    media =  sum(lista)/len(lista) 
    lista.append(media)
    lista.sort()
    if media in lista:
        list.remove(lista,media)
        return lista[lista.index(media):]
    else:
        return lista[lista.index(media)+1:]