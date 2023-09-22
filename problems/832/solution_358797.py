def eh_quadrada(matriz):
    if matriz == []:
        return True
    
    if len(matriz) == len(matriz[0]):
        return True
    
    else:
        return False