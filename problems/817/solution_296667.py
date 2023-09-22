def acima_da_media(notas: list[float]):
    media = sum(notas)/len(notas) 
    notas.append(media)
    notas.sort()
    b = notas
    a = str.find(b, media)
    c = media
    r = str(notas)
    s = str.find(r,c)
    return a