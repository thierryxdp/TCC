def eh_quadrada(matriz):
    """Esta função recebe uma matriz e retorna se é uma matriz 
    quadrada ou não.
    Recebe: list
    Retorna Bool"""
    for i in range(len(matriz)):
        for i in range(len(matriz[0])):
            if len(matriz) == len(matriz[0]) or len(matriz) == []:
                return True
            if len(matriz) != len(matriz[0]):
                return False