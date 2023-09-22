def media_matriz(M):
    """função que retorna a média de todos os números da matriz M, não vazia, com duas casas decimais de precisão
    list -> float"""
    soma = 0
    elementos = len(M)*len(M[0])
    for i in range(len(M)):
        for j in range(len(M[i])):
            soma += M[i][j]
    media = soma/elementos
    return round(media,2)