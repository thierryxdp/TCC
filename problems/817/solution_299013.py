def acima_da_media(notas):
    media = sum(lista)/len(acima_da_media)
    notas_acima_media = []
    for nota in notas:
        if nota > media:
            notas_acima_media.append(nota)
    notas_acima_media.sort()
    return notas_acima_media