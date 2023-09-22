def conta_numero (numero, matriz):
    """Funcao que dado um numero inteiro e uma matriz de inteiros conta e retorna quantas vezes aquele numero aparece na matriz"""
    contador = 0
    for numero in len(matriz):
        for numero in len(matriz[0]):
            matriz.count(matriz[numero])
            contador += 1
    return contador