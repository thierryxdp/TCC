def filtra_pares(x):
    """Essa função retorna uma tupla com todos os numeros pares em ordem da tupla de entrada"""
    """tupla->tupla"""
    
    tuppar=[i for i in x if i%2 == 0]
    
    return tuple(tuppar)