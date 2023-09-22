def acima_da_media(notas):
    notas = notas_copia
    media = sum(notas)/len(notas)
    list.append(notas, media)
    list.sort(notas)
    list.reverse(notas)
    return notas