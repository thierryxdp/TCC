def media_matriz(matriz):
    '''recebe uma matriz de inteiros não vazia, e retorna a média de todos
    os números da matriz(com duas casas de precisão).
    list ->float'''
    soma =0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma +=matriz[i][j]
    numeros =len(matriz)*len(matriz[0])
    media =round(soma/numeros, 2)
    return media