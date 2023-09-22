def acima_da_media(lista):
    media = sum(lista)/len(lista)
    if media in lista:
        lista.sort()
        indice = lista.index(media)
        return lista[indice+1:]   
    if media not in lista:
        lista.append(media)
        lista.sort()
        indice = lista.index(media)
        return lista[indice+1:]