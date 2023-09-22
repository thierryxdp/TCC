def media_matriz(matriz):
    '''Função que retorna a média de todos os números presentes em uma matriz
    de inteiros não vazia; lista -> float'''
    l=len(matriz)
    c=len(matriz[0])
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma = soma + matriz[i][j]
            media = soma/(l*c)
    return round(media,2)