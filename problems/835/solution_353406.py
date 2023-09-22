def melhor_volta(matriz):
    m = matriz
    vencedor = []
    for i in range(0, len(m)):
        for j in range(0,len(m[0])):
            vencedor = min(m[i][j])
            return vencedor