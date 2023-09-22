def eh_quadrada(matriz):
    """Esta função recebe uma matriz e retorna se é uma matriz 
    quadrada ou não.
    Recebe: list
    Retorna Bool"""
    
    if len(matriz) == len(matriz[0]) or len(matriz) ==0:
           return True
    else:
        return False