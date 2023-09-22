def acima_da_media(notas):
    media = sum(notas)/len(notas)
    int(media)
    list.insert(notas, 0, media)
    list.sort(notas)
    return media