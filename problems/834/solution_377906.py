def media_matriz(matriz):
    '''Função que dada uma matriz de inteiros não vazia, retorna a média
    de todos os números da matriz
    list -> float'''
    
    soma = 0
    divisor = 0
    
    for i in matriz:
        for j in i:
            soma = soma + j
            divisor = divisor + 1
    media = soma/divisor
            
    return round(media, 2)