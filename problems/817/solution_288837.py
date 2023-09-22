def acima_da_media(notas):
    media = sum(notas)/len(notas)
    notas = notas + [media]
    list.sort(notas)
    indice = list.index(notas, media) + list.count(notas, media)
    notasacima = notas[indice:]
    return notasacima