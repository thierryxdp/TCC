def acima_da_media(notas,media):
    notas.append(media)
    list.sort(notas)
    acimadamedia=notas[list.index(notas,media)+1:]
    return acimadamedia