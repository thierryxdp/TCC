def eh_quadrada(matriz):
    """ Identifica se uma matriz é quadrada, retorna True se sim e
    False se ela não for
    list -> bool
    """
    if matriz == []:
        return True
    linha = len(matriz)
    coluna = len(matriz[0])
    if linha != coluna:
        return False
   
    return True