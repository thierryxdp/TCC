def conta_numero(numero, matriz):
    '''Dado um número inteiro e uma matriz de inteiros
    de tamanho qualquer, conta e retorna quantas vezes
    aquele número aparece na matriz
    int, list -> int'''
    contador = 0
    for i in range(len(matriz)):
        if numero in matriz[i]:
            contador += 1
    return contador