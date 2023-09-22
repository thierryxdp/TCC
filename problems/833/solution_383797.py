def conta_numero(numero,matriz):
    """faça uma função que dado um numero inteiro e uma matriz de inteiros de tamanho qualquer, conte e retorne quantas
    vezes aquele número aparece na matriz
    int, list -> int"""
    count = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
            	count = count + 1
    return count