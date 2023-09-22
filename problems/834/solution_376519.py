def media_matriz(matriz):
    somaNumeros = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            somaNumeros += matriz[i][j]
        elementosTotal = len(matriz) * len(matriz[0])
        media = somaNumeros / elementosTotal
        mediaFinal = round(media,2)
    return mediaFinal