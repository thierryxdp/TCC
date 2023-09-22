def media_matriz(matriz):
    '''
    Recebe uma matriz de inteiros não vazia, e retorna 
    a média de todos os números da matriz com duas casas 
    decimais de precisão.
    list(list) -> float
    '''
    num = 0
    den = 0
    for i in matriz:
        for j in i:
            num = num + j
            den = den + 1
    return round(num/den, 2)