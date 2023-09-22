def acima_da_media(notas):
    """Recebe uma lista com valores e retorn aqueles maiores
    	que a media destes
        list -> list"""
    media = sum(notas)/len(notas)
    notas.append(media)
    notas.sort()
    redondo = int(round(media))
    if redondo in notas[notas.index(media)+1:]:
        acima = notas[notas.index(media+2):]
    else:
        acima = notas[notas.index(media)+1:]
    return acima