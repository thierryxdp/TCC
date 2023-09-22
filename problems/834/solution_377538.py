def media_matriz(matriz):
    ''' Função que determina a média dos números de uma dada matriz
    list -> float '''
    n = len(matriz)*len(matriz[0])
    soma = 0
    for i in list(range(len(matriz))):
        for j in list(range(len(matriz[0]))):
            soma = soma + j
    return soma/n