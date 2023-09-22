def eh_quadrada(matriz):
    """
    recebe uma matriz e retorna um valor booleano respondendo se
    essa é quadrada ou não.
    """
    if matriz ==[]:
        return True    
    if len(matriz)==len(matriz[0]):
        return True
    else:
        return False