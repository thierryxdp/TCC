def conta_numero(numero, matriz):
    '''
    funcao que dado um numero inteiro e uma matriz apenas
    composta por inteiros e de tamanho qualquer, retorna
    a quantidade de vezes que o numero fornecido como argu
    mento aparece na matriz
    dados de entrada: int, list
    retorna: int
    '''
    contador = 0
    if len(matriz) == 0:
        return 0
    else:
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if matriz[i][j] == numero:
                    contador = contador + 1
    return contador