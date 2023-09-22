def eh_quadrada(matriz):
    """Dada uma matriz, a função retornará um booleano informando True
    caso a matriz seja quadrada e False caso não seja.
    matriz -> bool"""
    
    if len(m) == 0:
        return bool(1)
    
    elif len(m) == len(m[0]):
        return bool(1)
    
    elif len(m) != len(m[0]):
        return bool(0)