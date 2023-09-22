def eh_quadrada(matriz):
    """..."""
    matriz = []
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == j:
                return "True"
            elif i == 0:
                return "True"
            else:
                return "False"