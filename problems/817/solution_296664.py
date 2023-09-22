def acima_da_media(notas: list[float]):
    media = sum(notas)/len(notas) 
    notas.append(media)
    notas.sort()
    r = str(notas)
    s = str.find(r,media)
    return notas[s:]