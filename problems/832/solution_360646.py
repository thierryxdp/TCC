def eh_quadrada(matriz):
    if len(matriz) == 0:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else: 
        return False