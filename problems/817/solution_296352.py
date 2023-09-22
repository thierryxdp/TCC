def acima_da_media(notas):
    media = sum(notas)/len(lista)
    notas.append(media)
    notas.sort()
    pos_media = notas.index(media)
    return notas[pos_media+1:]