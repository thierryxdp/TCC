def acima_da_media(notas):
    media=sum(notas)/len(notas)
    notas.sort()
    if media in notas:
        notas.remove(media)
        indice=notas.index(media)
        return notas[indice+1:]
    else:
        notas.append(media)
        indice=notas.index(media)
        return notas[indice+1:]