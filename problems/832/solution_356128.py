def eh_quadrada(matriz):
    '''Função que diz se a matriz de entrada é quadrada ou não. Retorna True se for quadrada, caso contrário retorna False'''
    linha = len(matriz)
    coluna = len(matriz[0])
    if matriz == [] or linha != coluna:
        return False
    else:
        return True