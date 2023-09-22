def eh_quadrada(matriz):
    """Função na qual dada uma matriz, verifica se ela é quadrada ou não."""
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if len(matriz) == 0:
                return False
                if matriz[i][j] != matriz[j][i]:
                    return False
    return True