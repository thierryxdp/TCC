def melhor_volta(matriz):
    for i in range(6):
        for j in range(10):
            tempo=min(matriz[i][j])
            melhor_volta=tempo[j]
            volta=tempo[i]
    return (melhor_volta,tempo,volta)