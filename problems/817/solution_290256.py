def acima_da_media(notas, m):
    notas_acima_da_media = list()
    for c in notas:
        if c >= m:
            notas_acima_da_media.append(c)
    return notas_acima_da_media