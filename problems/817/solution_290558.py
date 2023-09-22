def acima_da_media(notas):
    media = list.sum(notas)//2
    list.insert(notas, media)
    return notas