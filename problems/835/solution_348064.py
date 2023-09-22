def melhor_volta(matriz):
    melhor=matriz[0]
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j]<melhor:
                melhor=matriz[i][j]
    return melhor