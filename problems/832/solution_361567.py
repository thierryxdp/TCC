def eh_quadrada(matriz):
    '''Função que identifica se a mtriz dada de entrada é quadrada
    list -> bool'''
    if matriz == []:
        return True
    linha = len(matriz)
    coluna = len(matriz[0])
    if linha == coluna:
        return True
    else:
        return False