def conta_numero(numero, matriz):
    '''Função que dado um número inteiro e uma matriz, conta e
    retorna quantas vezes aquele número aparece na matriz
    int, list -> int'''
    vezes = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
            	vezes = vezes + 1
    return vezes