def acima_da_media(lista):
    media = sum(lista)/ len(lista)
    list.append(lista,media)
    list.sort(lista)
    lista1 = lista[list.index(lista,media)+1:]
    if media in lista1:
        list.remove(lista1, media)
    return lista1