def acima_da_media(lista):
    media = sum(lista)/len(lista)
    media1 = round(media)
    lista.append(media1)
    lista.sort()
    indice = lista.index(media1)
    return lista[indice+1:]