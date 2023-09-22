def eh_quadrada(matriz):
    """Função que identifica se uma matriz  é quadrada
    list -> float"""
    zeros = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 0:
                return True
            elif matriz[i][j] > 0:
                return False