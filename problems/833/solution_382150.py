conta_numero(numero, matriz):
    '''Dado um número inteiro e uma matriz de inteiros, conta e retorna quantas vezes aquele número aparece na matriz
    int, list -> int'''
    total = 0
    for i in len(matriz):
        total = total + list.count(matriz[i], numero)
    return total