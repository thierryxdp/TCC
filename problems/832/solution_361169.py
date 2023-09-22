def eh_quadrada(m):
    """Função booleana que identifica se a matriz de entrada m é quadrada ou não. Lista->Bool"""
    if m==[]:
        return True
    elif len(m)==len(m[0]):
        return True
    else: return False