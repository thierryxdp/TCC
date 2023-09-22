def acima_da_media(notas):
    """ """
    media= sum(notas) / len(notas)
    if media not in notas:
        notas.insert(0,media)
    notas.sort()
    ind=notas.index(media)
    return notas[ind+1:]