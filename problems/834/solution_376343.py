def media_matriz(matriz):
    '''Retorna a média de todos os numeros de uma matriz com precisão de duas casas
       list -> float'''
    n = 0
    mediano = 0
    for i in matriz:
        for j in i:
            n = n + j
            mediano += 1
    x = n/mediano
    return round(x,2)