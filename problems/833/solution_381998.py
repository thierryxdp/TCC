def conta_numero (n, matriz):
    'dado um numero inteiro e uma matriz, retorna quantas vezes o numero aparece na matriz. int, str -> int'
    count = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == n:
                count = count + 1
    return count