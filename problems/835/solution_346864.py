def melhor_volta(matriz):
    melhor_tempo = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]< matriz[i][j+1]:
                melhor_tempo = matriz[i][j]
    return (i, melhor_tempo, j)