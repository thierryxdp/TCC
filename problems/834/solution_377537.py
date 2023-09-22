def media_matriz(m):
    ''' Função que determina a média dos números de uma dada matriz m
    list -> float '''
    n = len(matriz)*len(matriz[0])
    soma = 0
    for i in list(range(len(matriz))):
        for j in list(range(len(matriz[0]))):
            soma = soma + j
    return soma/n