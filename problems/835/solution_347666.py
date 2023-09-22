def melhor_volta(matriz):
    linhas=len(matriz)
    colunas=len(matriz[0])
    for i in range(linhas):
        for j in range(colunas):
            tempo=min(matriz[i][j])
            melhor_volta=tempo[j]
            volta=tempo[i]
    return tempo,melhor_volta,volta