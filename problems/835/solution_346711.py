def melhor_volta(matriz):
    minimo=min(matriz)
    for i in range(6):
        for j in range(10):
            if [i][j]==minimo:
                minimo=[i][0]
    return minimo