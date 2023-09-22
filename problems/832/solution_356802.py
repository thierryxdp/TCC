def eh_quadrada(matriz:list)->bool:

    """ Função que receb uma matriz como entrada matriz e retorna
        se é quadrada ou não. """
    nlinhas = len(matriz)
    ncolunas = len(matriz[0])
    
    if nlinhas == 1 and ncolunas == 0:
        return True
    elif nlinhas == ncolunas:
        return True
    else:
        return False