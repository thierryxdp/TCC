def eh_quadrada(matriz):
    """
    list -> bool
    """
    # matriz vazia
    if matriz == []:
        return True
    # matriz coluna e matriz NxM
    elif type(matriz[0]) == list:
        return len(matriz) == len(matriz[0])
    # matriz lina
    else:
        return len(matriz) == 1 # matriz linha só é quadrada quando é 1x1