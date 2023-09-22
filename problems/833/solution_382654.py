def conta_numero(numero,matriz):
    """calculo e retorno de uma funçao que conta quantas vezes um numero aparece na matriz"""
    contador=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==numero:
                contador=contador+1
    return contador