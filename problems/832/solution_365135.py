def eh_quadrada(matriz):
    """Função que identifica se uma matriz  é quadrada
    list -> float"""
    zeros = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 0:
                zeros += 1
    total = len(matriz)*len(matriz[0])
    if (total - zeros) / total = 0:
        return True
    else:
        return False