def eh_quadrada(matriz):
    '''função que dado valores booleanos,receberar valores de saída como,true ou false'''
    linha = len(matriz)
    coluna = len(matriz[0])
    if matriz == [[]] or linha == coluna:
        return True
    return False