def melhor_volta(matriz):
    min_tempo = 999999
    melhor_volta = 0
    corredor = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] < min_tempo:
                melhor_volta = j+1
                corredor = i+1
                min_tempo = matriz[i][j]
    return (corredor, min_tempo, melhor_volta)