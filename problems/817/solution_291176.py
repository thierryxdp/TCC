def acima_da_media(lista):
    media = sum(lista)/len(lista)
    lista.append(media)
    lista.sort()
    indice = lista.index(media)
    return media, lista[indice+1:]