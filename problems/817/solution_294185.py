def acima_da_media(notas):
    """função que recebe uma lista de notas, calcula a média
    e retorna uma lista com as notas maiores que a media.
    list -> list"""
    media = sum(notas)/len(notas)
    if media in notas:
        notas.sort()
        x = list.index(notas, media)
        return notas[x+1:]

    else:
        inclui_media = notas + [media]
        inclui_media.sort()
        y = list.index(inclui_media, media)
        return inclui_media[y+1:]