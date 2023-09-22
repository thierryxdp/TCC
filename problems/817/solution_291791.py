def acima_da_media(notas):
    media=sum(notas)/len(notas)
    notas.append(media)
    notas.sort()
    return notas[(notas.index(media)+1):]