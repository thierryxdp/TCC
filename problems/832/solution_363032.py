def eh_quadrada(matriz):
    """
    função que verifica se uma matriz é quadrada
    list -> Boolean
    """

    for i in range(len(matriz)):
        if len(matriz[i]) != len(matriz):
            return False
    
    return True