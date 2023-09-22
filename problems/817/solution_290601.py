def acima_da_media(notas):
    media = sum(notas)//len(notas)
    list.insert(notas, media, 0)
    list.sort(notas)
    posicao = list.index(notas, media) + 1
    return notas[posicao:]