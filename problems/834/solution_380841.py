def conta_numero(numero, matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==numero:
                soma += matriz[i][j]
    return soma / (len(matriz) + len(matriz[0]))