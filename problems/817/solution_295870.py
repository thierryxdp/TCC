def acima_da_media(notas):
    '''
    '''
    media = int(sum(notas) / len(notas))
    notas.append(media)
    notas.sort()
    indice = notas.index(media)
    return notas[indice+1:]