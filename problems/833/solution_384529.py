def conta_numero(numero,matriz):
    '''dado um número inteiro(numero) e uma matriz de inteiros de tamanho
    qualquer, conta e retorna quantas vezes aquele número aparece na matriz;
    int, list -> int'''
    total = 0
    for i in matriz:
        total = total + i.count(numero)
    return total