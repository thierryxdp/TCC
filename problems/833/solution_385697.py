def conta_numero(numero,matriz):
    '''dado um numero inteiro(numero) e uma matriz(matriz) de inteiros,
    retorna quantas vezes o (numero) aparece na matriz; int, list -> int'''
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == numero:
                soma += 1
    return soma