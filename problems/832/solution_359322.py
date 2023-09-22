def eh_quadrada(matriz):
    """Retorna um valor booleano caso a matriz de entrada seja quadrada.
    lista --> booleano"""
    
    for i in range(len(matriz)):
        if len(matriz) == len(matriz[i]):
            return True
        elif len(matriz) == []:
            return True
        else:
            return False