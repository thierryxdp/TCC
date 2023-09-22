def eh_quadrado(matriz):
    """..."""
    matriz = []
    for i in range(len(matriz)):
        for i in range(len(matriz)):
            matriz[i][j] = matriz[i][j] + 1 
            if i == j:
                return 'True'
            elif i == 0:
                return 'True'
            else:
                return 'False'