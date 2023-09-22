def acima_da_media(notas):
    media=(sum(notas))/len(notas)
    if media in notas:
        notas.sort()
        indice=notas.index(media)
        nova_lista=notas[:]
    if media not in notas:
        nova_lista=notas
        notas.append(media)
        notas.sort()
        indice=notas.index(media)
    return nova_lista[indice+1:]