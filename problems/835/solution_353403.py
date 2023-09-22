def melhor_volta(matriz):
    m = matriz
    vencedor = []
    for i in range(4, len(m[0])):
        vencedor = min(m[i])
        return vencedor