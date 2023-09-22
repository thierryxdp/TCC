def media_matriz(matriz):
    '''Retorna a média de todos os números da matriz dada (com precisão de duas casa decimais);
    list(list) -> float'''
    numeros = 0
    total = len(matriz) * len(matriz[0])
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            numeros = numeros + matriz[i][j]
            
    return round(numeros/total, 2)