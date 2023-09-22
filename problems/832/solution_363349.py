def eh_quadrada(matriz):
    """A função retorna identifica se uma matriz é quadrada
    matriz(list)-->bool"""
    
    if len(matriz)==0:
        return True 
    for x in range(len(matriz)):
        if len(matriz) == len(matriz[0]):
            return True
    else:
        return False