def conta_numero(matriz,inteiro):
    count=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == inteiro:
                count += 1
    return count