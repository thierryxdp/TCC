def acima_da_media(notas):
    media = sum(notas)/len(notas)
    notas = notas + [media]
    list.sort(notas)
    indice = list.index(lista, media) + list.count(lista, media)
    notasacima = notas[indice:]
    return notasacima