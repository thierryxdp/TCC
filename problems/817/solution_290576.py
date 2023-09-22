def acima_da_media(notas):
    media= sum(notas)/len(notas)
    notas.sort
    index= notas.index(media)
    return index