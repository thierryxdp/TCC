def media_matriz(matriz:list)->float:
    soma=0
    total=0
    for i in range(len(matriz)):
        soma+=sum(matriz[i])
        total+=len(matriz[i])
    media=soma/total
    return round(media,2)