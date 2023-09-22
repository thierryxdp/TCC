def melhor_volta(matriz):
    for c in range(len(matriz)):
        for t in matriz[c]:
            return min(matriz[c])