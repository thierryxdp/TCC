def acima_da_media(notas):
    notas2 = notas[:]
    media = sum(notas)/len(notas)
    list.insert(notas, 0, media)
    list.sort(notas)
    if media in notas2:
        return notas[list.index(notas,media)+1:]