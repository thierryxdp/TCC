def media_matriz(matriz):
    '''Função que recebe uma matriz de inteiros não vazia e retorna a média entre
    seus elemenos'''
    '''list(list(int)) --> float'''
    i = 0
    j = 0
    soma_elementos = 0
    posicoes = 0
    while i < len(matriz):
        for j in matriz[i]:
    		soma_elementos += matriz[i][j]
    i = i + 1
    posioes += 1
    return soma_elementos/posicoes