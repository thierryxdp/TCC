def media_matriz(matriz):
    '''
    função que dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz;
    list(list) -> float
    '''
    media = 0
    for linha in matriz:
        for aij in linha:
            media = media + aij
    return media