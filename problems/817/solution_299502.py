def acima_da_media(lista):
    media = sum(lista)/len(lista)
    list.append(lista, media)
    list.sort(lista)
    n = list.index(lista, media)
    while media in lista:
        list.remove(lista, media)
    return lista[n :]