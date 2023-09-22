def eh_quadrada(matriz):
    """Função que inentifica se uma matriz é quadrada
    matriz->booleano"""
    
    if matriz == []:
        return True
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False