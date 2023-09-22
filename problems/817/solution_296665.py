def acima_da_media(notas: list[float]):
    media = sum(notas)/len(notas) 
    notas.append(media)
    notas.sort()
    c = media
    r = str(notas)
    s = str.find(r,c)
    return notas[s:]