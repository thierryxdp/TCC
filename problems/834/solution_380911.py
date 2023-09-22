def media_matriz(matriz):
    '''dada uma matriz e calcula a media de todos os numeros na matriz
    :param matriz: list->list
    :return: float->float
    '''
    soma = 0
    tamanho = 0
    media = 0
    if matriz !=[]:
        for lin in range(0, len(matriz)):
                 tamanho += 1
                soma += matriz[lin][col]
                media = soma / tamanho
        return  round(media, 2)