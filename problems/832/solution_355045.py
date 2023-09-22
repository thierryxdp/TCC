def ehquadrada(matriz):
    """Função que identifica de uma matriz é quadrada ou não.
        matriz->bool"""
    
    if len(matriz)==len(matriz[0]):
        return True
    else:
        return False