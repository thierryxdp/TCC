def media_matriz(matriz):
    soma = 0
    for i, valores in enumerate(matriz):
        if i <= len(matriz):
            soma = soma + valores
    media = soma / len(matriz)
    return media