def eh_quadrada(matriz: list) -> bool:
    """ Indentifica se a matriz dada como parametro de entrada é quadrada
    (M(mxn) onde m=n).
    list(list)-> bool """
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False