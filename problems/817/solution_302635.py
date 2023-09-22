def acima_da_media(lista):
    media= sum(lista)/ len(lista)
    if media not in lista:
        lista.append(media)
    lista.sort()
    x= lista.index(media)
    lista2 = lista[x+1:]
    y= lista2.count(media)
    return lista2[y:]