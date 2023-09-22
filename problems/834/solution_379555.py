def media_matriz(matriz):
    '''Função que dada uma matriz de inteiros não vazia, retorna a media de tosos os numeros da matriz:
    list -> float'''
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma = soma + matriz[i][j]
    n = len(matriz) * len(matriz[0])
    media = soma/n
    return round(media,2)