def media_matriz(matriz):
    """Calcula e retorna a média de todos os números da matriz com duas casa decimais
    matriz -> list
    contador -> int
    """
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            contador = contador + matriz[i][j]
    return round(contador/(len(matriz)*len(matriz[0])),2)