def acima_da_media(notas):
    media = sum(notas)/len(notas)
    return media, acima_da_media(notas, media)