def media_matriz(matriz):
    media = 0
    for i in range(matriz):
        for j in range(matriz):
            media = media + matriz[i][j]
            media = media / 15
    return(media)