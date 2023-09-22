def eh_quadrada(matriz):
    for i in matriz:
        if len(matriz) != len(i):
            return False
    return True