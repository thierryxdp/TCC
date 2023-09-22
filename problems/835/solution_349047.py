def melhor_volta(matriz):
    melhor = [-1,999999, -1]
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
            if matriz[i][j] < melhor[1]:
                melhor[0] = i
                melhor[1] = matriz[i][j]
                melhor[2] = j
    return tuple(melhor)