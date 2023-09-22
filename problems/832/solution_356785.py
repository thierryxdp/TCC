def eh_quadrada(matriz:list)->bool:
    """Identifica se a matriz inserida é quadrada ou não
       
       Parameters:
       matriz: matriz a ser analisada
       
       Returns:
       True para é quadrada e False para não quadrada
    """
    if matriz == []:
        return True
    else:
        nlin = len(matriz)
        ncol = len(matriz[0])
        if nlin == ncol:
            return True
        else:
            return False