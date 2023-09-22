def filtra_pares(a,b,c,d):
    """função que retorna apenas os elementos pares de uma tupla
    tuple -> tuple"""
    tupla = [a,b,c,d]
    
    if tupla % 2 == 0:
        return tupla
    else:
        return False