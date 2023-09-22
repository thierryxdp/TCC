def acima_da_media(notas: list[float]):
    media = sum(notas)/len(notas) 
    notas.append(media)
    notas.sort()
    k = notas>media
    return k