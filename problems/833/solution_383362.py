ef conta_numero(N,matriz):

    """ Função que dado um número inteiro e uma matriz de inteiros de tamanho qualquer, conta e
    retorna quantas vezes aquele número aparece na matriz."""
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == N:
               contador += 1
    return contador