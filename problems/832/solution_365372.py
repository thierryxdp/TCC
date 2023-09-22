def eh_quadrada(matriz):
    """list(list) -> bool"""
    """retorna se a matriz é quadrada"""
    
    if len(matriz) == 0:
        return True
    
    elif len(matriz) == len(matriz[0]):
        return True
    
    else:
        return False