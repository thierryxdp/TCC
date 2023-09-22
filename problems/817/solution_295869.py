def acima_da_media(notas):
    '''
    '''
    media = sum(notas) / len(notas)
    notas.append(int(media))
    notas.sort()
    indice = notas.index(media)
    return notas[indice+1:]