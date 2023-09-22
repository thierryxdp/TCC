def media_matriz(matriz):
    '''Dada uma matriz de inteiros não vazia, retorna
    a média de todos os números da matriz com duas
    casas decimais de precisão
    list -> float'''
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma += matriz[i][j]
    media = round(soma / (i + 1)*(j + 1), 2)
    return media