def media_matriz(matriz):
    """
    Função recebe uma matriz de inteiros não vazia e retorna a média
    de todos os números da matriz(com duas casas decimais de precisão).
    matriz -> float
    """
    numerador=0
    divisor=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            numerador+=matriz[i][j]
            divisor+=1
   	
    media=numerador/divisor
    return round(media,2)