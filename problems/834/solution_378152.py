def media_matriz(matriz: int) -> float:
    """Essa função, dada uma matriz de números inteiros não vazias,
    retorna a média de todos os números da matriz com precisão 
    de duas casas decimais"""
    numeros = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            numeros += matriz[i][j]
    media = numeros/2
    return round(media,2)