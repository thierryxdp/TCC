def acima_da_media(notas):
    media = sum(notas)//len(notas)
    sorted(media)
    x = media.index(notas)
    del media[0:x+1]
    return media