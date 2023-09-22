def acima_da_media(notas):
    """Recebe uma lista com valores e retorn aqueles maiores
    	que a media destes
        list -> list"""
    import math
    media = sum(notas)/len(notas)
    notas.append(media)
    notas.sort()
    if not media%1 >0:
        redondo = int(math.floor(media))
    	if redondo in notas[notas.index(media)+1:]:
        	acima = notas[notas.index(redondo)+1:]
    else:
        acima = notas[notas.index(media)+1:]
    return acima