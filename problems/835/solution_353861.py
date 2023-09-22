def melhor_volta(matriz):
    corredor=0
    tempo=0
    volta=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            corredor=corredor+[min(matriz[i])]
            tempo=tempo+[min(matriz)]
            volta=volta+[min(matriz[i][j])]
    return (corredor, tempo, volta)