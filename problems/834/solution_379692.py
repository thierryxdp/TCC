def media_matriz(matriz):
    """
    Função que recebe uma matriz e retorna a média da soma dos números da matriz
    list -> float
    """
    soma = 0
    media = 0 
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma = matriz[i][j] + matriz[j][i]
            media = soma/len(matriz)
    return round(media,2)