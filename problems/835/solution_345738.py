def melhor_volta(matriz):
    minimos = []
    for i in range(len(matriz)):
        minimos += min(matriz[i])
    return minimos