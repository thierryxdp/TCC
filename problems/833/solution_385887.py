def conta_numero(numero, matriz):
    '''Função que dado um número inteiro e uma matriz de inteiros, retorna quantas vezes aquele número aparece na matrriz.'''
    '''int,list(list)->int'''
    conta = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                conta = conta + 1
    return conta