def conta_numero(numero, matriz):
    '''função que dado um número inteiro e uma matriz de inteiros, conta e retorna quantas vezes o número aparece
    na matriz.
    int, list -> int'''
    
    conta = 0
    
    for n in len(matriz):
        if numero in matriz[n]:
            conta = conta + 1
    return conta