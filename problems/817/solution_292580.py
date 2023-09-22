def acima_da_media(notas):
    """A função retorna as notas acima da média na lista
    list -> list"""
    media=sum(notas)/len(notas)
    notas.sort()
    if media in notas:
        indice=notas.index(media)
        return notas[indice+1:]
    else:
        notas.append(media)
        notas.sort()
        indice=notas.index(media)
        return notas[indice+1:]