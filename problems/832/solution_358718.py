def eh_quadrada(matriz):
    """idenfica se uma matriz é quadrada;
    matriz, -> strin"""
    m = matriz
    
    if m == []:
        return 'True'
    elif len(m) == len(m[0]):
        return True
    else:
        return False