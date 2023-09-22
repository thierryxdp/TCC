def eh_quadrada(matriz):
    """..."""
    matriz = []
    for i in range(matriz):
        if len(matriz) == 0:
            return 'True'
        elif len(matriz) == len(matriz[i]):
            return 'True'
        else:
            return 'False'