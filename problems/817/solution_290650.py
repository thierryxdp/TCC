def acima_da_media(notas):
    media = sum(notas)//len(notas)
    list.insert(notas, 0, media)
    list.sort(notas)
    list.reverse(notas)
    posicao = list.index(notas, media)
    list.reverse(notas)
    return notas[:posicao]