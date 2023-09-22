def media_matriz(matriz):
    media = 0
    for i in range(3):
        for j in range(5):
            media = media + matriz[i][j]
            media = media / 15
    return(media)