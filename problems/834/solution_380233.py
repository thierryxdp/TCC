def media_matriz(matriz):
    '''dada uma matriz, retorna a média de todos os números
    dentro dela
    list-> float
    '''
    soma = 0
    total = len(matriz)*len(matriz[0])
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
    media = round(soma / total,2)
    
    return media