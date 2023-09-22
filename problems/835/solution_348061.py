def melhor_volta(matriz):
    melhor<10000
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if voltas[i][j]<melhor:
                melhor=voltas[i][j]
    return melhor