def eh_quadrada(matriz):
    """Retorna um valor booleano caso a matriz de entrada seja quadrada.
    lista --> booleano"""
    
    if matriz == []:
        return True
    
    for i in range(len(matriz)):
        if len(matriz) == len(matriz[i]):
            return True
        else:
            return False