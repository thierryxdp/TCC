def media_matriz(matriz):
    soma=0
    total=0
    for i in len(matriz):
        soma+=sum(matriz[i])
        total+=len(matriz[i])
    media=soma/total
    return round(media,2)