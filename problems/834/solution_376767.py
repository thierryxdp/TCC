def media_matriz(matriz):
    '''Funcao que recebe uma matriz com numeros
inteiros e retorna a media de todos os numeros da
matriz'''
    soma = 0
    for linha in matriz:
        for coluna in linha:
            contCol += 1
            soma += matriz[linha][coluna]
            media = soma/contCol
    return round(media,2)