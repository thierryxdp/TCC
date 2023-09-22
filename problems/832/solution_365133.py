def eh_quadrada(matriz):
    """Função que identifica se uma matriz  é quadrada
    list -> float"""
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == 0:
                return True
            else:
                return False