def eh_quadrada(matriz):
    """Função que retorna um valor boleano caso a matriz seja quadrada ou não
    int-> bool"""
    if len(matriz) == 0:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False