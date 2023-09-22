def media_matriz(matriz):
    '''Calcula a média de todos os valores da matriz.
    list -> float
    '''
    soma = 0
    h = 0
    media = 0
    if matriz != []:
        for l in range(len(matriz)):
            for c in range(len(matriz[l])):
                h += 1
                soma += matriz[l][c]
                media = soma / h

    return round(media, 2)