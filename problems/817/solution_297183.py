def acima_da_media(notas):
    media = sum(notas)//len(notas)
    media =  list.insert(media,0,notas)
    media.sort()
    x = media.index(notas)
    del media[0:x+1]
    return media