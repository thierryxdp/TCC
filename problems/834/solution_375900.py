# Média da Matriz
def media_matriz(matriz):
    '''Ao receber um amatriz de números inteiros não vazia, retorna
    a média de todos os números da matriz, com duas casas de precisão;
    INT -> FLOAT'''
    numElement = len(matriz)*len(matriz[0])
    soma = 0
    for i in matriz:
        for j in i:
            soma += j
    return round((soma/numElement),2)