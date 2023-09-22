def acima_da_media(notas):
    media = sum(notas)/len(notas)
    return media, elementosMaiores(notas, media)