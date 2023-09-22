def acima_da_media(notas):
    if media not in notas:
    media=sum(notas)/len(notas)
    notas.append(media)
    notas.sort()
    i=notas.index(media)
    return notas[i+1:]