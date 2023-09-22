def eh_quadrada(matriz):
    """Funcao que identifica se a matriz fornecida é quadrada ou não;
    list(list) -> bool"""
    
    if matriz == [] or len(matriz) == len(matriz[0]):
        return True
    
    else:
        return False