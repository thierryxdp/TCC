def eh_quadrada(matriz):
    for i in range(len(matriz)):
        if len(matriz) == len(matriz[i]):
            return True
        else:
            return False