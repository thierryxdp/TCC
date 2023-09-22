def media_matriz(matriz):
    '''Dada uma matriz de inteiros no vazia, retorna a media de todos os numeros da matriz;
    list -> float'''
    soma = 0
    divisor = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
            divisor += 1

    return round((soma/divisor),2)