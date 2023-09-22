def conta_numero(n, matriz):
    total = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == n:
                total = total + 1
    return total