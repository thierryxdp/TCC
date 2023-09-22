def melhor_volta(matriz):
    m = matriz
    vencedor = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            vencedor = min([m[i][j]])
            return vencedor