def media_matriz(matriz):
    '''Dada uma matriz de inteiros não fazia, retorna a média de todos os números da matriz, com exatamente duas casas decimais de precisão
    list -> float'''
    total = 0
    qnts = 0
    media = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            total = total + matriz[i][j]
            qnts = qnts + 1
    media = total / qnts
    return round(2, media)