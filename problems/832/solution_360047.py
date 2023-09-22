def eh_quadrada(matriz):
    """Função que retorna se uma matriz é quadrada ou não."""
    """List -> Boolean"""
    if len(matriz) == 0:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False