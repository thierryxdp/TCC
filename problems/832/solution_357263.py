def eh_quadrada(matriz):
    """Identifica se a matriz dada é ou não quadrada.
       list -> bool"""
    
    if len(matriz) == len(matriz[0]):
        return True
    elif len(matriz) == 0:
        return True
    else:
        return False