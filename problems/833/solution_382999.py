def conta_numero(numero,matriz):
    '''A função recebe um número inteiro e uma matriz de inteiros de tamanho qualquer e
    retorna a quantidade de vezes que aquele número aparece na matriz
    int, list -> int'''
    count=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==numero:
                count=count+1
    return count