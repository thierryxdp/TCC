def eh_quadrada(matriz):
    """Função na qual dada uma matriz, verifica se ela é quadrada ou não."""
    for i in range(len(matriz)):
        for j in range(len(matriz[0:])):
            if matriz[i][j] != matriz[i][j]:
                return False
    return True