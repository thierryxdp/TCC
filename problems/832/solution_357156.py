def eh_quadrada(matriz):
    
    if len(matriz) == 0:
        quad = True
    elif len(matriz) == len(matriz[0]):
        quad = True
    else:
        quad = False
    
    return quad