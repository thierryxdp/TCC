def media_matriz(matriz):
    ''' função que recebe como entrada uma matriz de números inteiros,
        NÃO VAZIA, retornando a média entre os números da matriz
        [list-->float]'''

    A = len(matriz)
    B = len(matriz[0])
    
    soma = 0
    TOTAL = A*B

    for sublista in matriz:
        for inteiro in sublista:
            soma += inteiro
            
    return round(soma/TOTAL,2)