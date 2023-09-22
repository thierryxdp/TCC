def acima_da_media(notas):
    media = sum(notas)//len(notas)
    y= sorted(media)
    x = y.index(notas)
    del media[0:x+1]
    return media