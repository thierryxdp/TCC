def eh_quadrada(matriz):
    while len(matriz)>0:
        if (len(matriz) == len(matriz[0])):
            return True
        else:
            return False
    if (len(matriz) == 0):
        return True