def media_matriz(matriz):
    '''Funcao que recebe uma matriz com numeros
inteiros e retorna a media de todos os numeros da
matriz'''
    soma = 0
    elementos = 0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            elementos += 1
            soma += matriz[linha][coluna]
            media = soma/elementos
    return round(media,2)