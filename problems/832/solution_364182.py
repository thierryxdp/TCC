def eh_quadrada(matriz):
    """
    Essa função ira retornar se uma matriz dada como argumento se trata
    de uma matriz quadrada ou nao.
    list->bool
    """
    
    #caso seja uma matriz vazia
    if matriz == []:
        return True
    
    else:
        if len(matriz) == len(matriz[0]):
            return True
        else:
            return False