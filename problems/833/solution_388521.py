def conta_numero(numero,matriz):
    ''' dado um numero inteiro e uma matriz, conta e retorna
    quantas vezes aquele numero aparece na matriz;
    int,matriz-> int'''
    conta = 0
    for i in range(len(matriz)):
        for i in (matriz[i]):  
            if i == numero:
            conta= conta + 1
    return conta