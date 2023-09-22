def acima_da_media(notas):
    notas_media = []
    media = sum(notas)/len(notas)
    for i in range (len(notas)):
        if notas[i] > media:
            notas_media.append(notas[i])
    notas_media.sort()
    return notas_media