def acima_da_media(notas):
    media = sum(notas)/len(notas)
    list.insert(notas, 0, media)
    list.sort(notas)
    if media in notas:
        return notas[list.index(notas,media)+1:]