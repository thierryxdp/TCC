def media_matriz(matriz):
    '''
    dado uma matriz apenas contendo numeros inteiros, retorna
    a media de todos os seus elementos
    dados de entrada: list
    retorna: float
    '''
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma = soma + matriz[i][j]
    return round(soma/(len(matriz)*len(matriz[0])),2)