def melhor_volta(matriz):
    corredor=0
    tempo=0
    volta=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            corredor=matriz.index(min(matriz[i]))
            tempo=min(matriz[i])
            volta=matriz.indez(min(matriz[i][j]))
    return (corredor,tempo,volta)