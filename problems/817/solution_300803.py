def acima_da_media(lista):
    '''Retorna uma lista ordenada com as notas que ficaram acima da media.'''
    media = (sum(lista)/len(lista))
    if media not in lista:
        lista.append(media)
    lista.sort()
    return lista[lista.index(media)+1:]