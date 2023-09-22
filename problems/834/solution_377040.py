def media_matriz(matriz):
    '''Dado uma matriz, retorna a média de todos os números dela. list -> float'''
    soma = 0
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
            soma += matriz[i][j]
    media = soma/(len(matriz)*len(matriz[0]))
    return round(media,2)