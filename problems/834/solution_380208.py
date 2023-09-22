def media_matriz(matriz):
    '''função que recebe uma matriz de inteiros e retorna a média de todos os números da matriz
    list -> float'''
    t = 0
    for x in range(len(matriz)):
        for z in range(len(matriz[x])):
            	t = t + matriz[x][z]
    return round((t)/(len(matriz[0]) * len(matriz)), 2)