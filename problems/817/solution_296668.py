def acima_da_media(notas: list[float]):
    media = sum(notas)/len(notas) 
    notas.append(media)
    notas.sort()
    b = notas
    c = media
    return b