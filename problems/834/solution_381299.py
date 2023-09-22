def media_matriz(m):
    soma=0
    for linha in m:
        soma+= sum(linha)
    media = soma/(len(m[1])*len(m))
    return round(media, 2)