def conta_numeros(numero, matriz):
    """Função que dado um número inteiro(numero) e uma matriz de
    inteiros(matriz) retorne quantas vezes o número apareceu na matriz.
    int, lista -> int"""

    num = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if str(numero) in str(matriz[i][j]):
                num += 1

    return num