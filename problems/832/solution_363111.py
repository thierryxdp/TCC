def eh_quadrada(matriz):
    """A função recebe uma matriz (lista) e retorna True se for 
    quadrada e False caso não seja."""
    for i in matriz:
        for j in i:
            if len(matriz) == len(matriz[i][j]):
                return True
            else:
                return False