def media_matriz(matriz):
    '''
        recebe uma matriz e retorna a media de todos os elementos dessa matriz
        entrada: lista
        saida: float
    '''
    somaNum = 0
    contaElem = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            somaNum = somaNum + matriz[i][j]
            contaElem = contaElem + 1
    return round(somaNum/contaElem, 2)