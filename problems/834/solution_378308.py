def media_matriz(matriz):
    """recebe uma matriz de inteiros nao vazia e retorna a media de todos os
    numeros dessa matriz
    list -> float"""
    
    linha = len(matriz)
    coluna = len(matriz[0])
    soma = 0
    
    for i in range(linha):
        for j in range(coluna):
            soma += matriz[i][j]
            
    media = soma / (linha * coluna)
    
    return round(media, 3)