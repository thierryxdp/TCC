def media_matriz(matriz):
    ''' Função que determina a média dos números de uma dada matriz
    list -> float '''
    n = len(matriz)*len(matriz[0])
    for i in list(range(len(matriz))):
        soma = 0
        for j in list(range(len(matriz[i]))):
            soma = soma + j
    return soma/n