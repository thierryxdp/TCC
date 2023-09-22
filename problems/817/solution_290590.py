def acima_da_media(notas):
    media = sum(notas)//len(notas)
    list.insert(notas, media, 0)
    list.sort(notas)
    return media