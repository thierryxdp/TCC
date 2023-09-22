def media_matriz(matriz):
    '''Função que dada uma matriz de inteiros retorna a média de todos os números da matriz.
    list -> float'''
    soma = 0
    num_matriz = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma = soma + matriz[i][j] 
            num_matriz = num_matriz + 1
    media = soma / num_matriz
    return round(media,2)