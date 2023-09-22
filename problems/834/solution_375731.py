def media_matriz(matriz):
    """Esta função recebe uma matriz e retorna a media dos valores
    da matriz.
    Recebe: list
    Retorna: float"""
    numeros = []
    posmat = 0
    divisor = 0
    
    for posmat in range(len(matriz)):
        for i in range(len(matriz[posmat])):
            list.append(numeros, matriz[posmat][i])
            divisor = divisor + 1
    return round(sum(numeros)/divisor, 2)