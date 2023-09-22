def eh_quadrada(matriz):
    '''função que dado valores booleanos,receberar valores de saída como,true ou false'''
    linha = len(matriz)
    coluna = len(matriz[0])
    if linha == coluna:
        return True
    if matriz == '':
        return True
    return False