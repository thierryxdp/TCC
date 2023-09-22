def acima_da_media(lista):
    """Retorna uma lista com as notas que ficaram a cima da media.List-->List"""
    media = (sum(lista)/len(lista))
    lista.sort()
    if media in lista:
        pos = lista.index(media)
    else:
        lista.append(media)
        lista.sort()
        pos=lista.index(media)
    return lista[pos+1:]