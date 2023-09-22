def media_matriz(matriz):
    """Calcula e retorna a média de todos os numeros de uma matriz
    list -> float
    """
    soma = 0
    linha = len(matriz)
    coluna = len(matriz[0])
    for i in range(linha):
        for j in range(coluna):
            soma = soma + matriz[i][j]
    
    return round(soma/(linha*coluna),2)