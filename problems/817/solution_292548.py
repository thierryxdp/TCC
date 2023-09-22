def acima_da_media(notas):
    media=sum(notas)/len(notas)
    notas.append(media)
    notas.sort()
    indice=notas.index(media)
    notas.remove(media)
    return notas[indice:]