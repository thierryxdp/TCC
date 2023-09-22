def media_matriz(matriz):
    '''Calculo a média de dada matriz.
lista de int->float'''
    soma = 0
    media = 0
    tamanho = 0
    if matriz != []:
        for l in range(0, len(matriz)):
            for c in range(0, len(matriz[l])):
                tamanho += 1
                soma += matriz[l][c]
                media = soma / tamanho

    return round(media, 2)