def acima_da_media(notas):
    """Recebe uma lista com valores e retorn aqueles maiores
    	que a media destes
        list -> list"""
    media = sum(notas)/len(notas)
    notas.append(media)
    notas.sort()
    acima = notas[notas.index(media)+1:]
    return acima