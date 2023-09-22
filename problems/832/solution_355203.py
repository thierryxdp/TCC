def eh_quadrada(matriz):
    """Função que calcula se a matriz dada de entrada é quadrada sim ou não retornando True ou False
    list -> bool"""
    if matriz != []:
        if len(matriz) == len(matriz[0]):
            return True
        else:
            return False
    else:
        return True