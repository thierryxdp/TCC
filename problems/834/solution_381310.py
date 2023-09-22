def media_matriz (matriz):
    """Funcao retorna a media de uma dada matriz
    list -> int"""
    soma = 0
    numeros = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
            numeros += 1
    return round(soma/numeros,2)