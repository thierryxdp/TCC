def eh_quadrada(matriz):
    '''Dado uma matriz retorna se ela é quadrada ou não. list -> bool.'''
    if matriz == []:
        return True
    conta_linha = len(matriz)
    conta_coluna = len(matriz[0])
    if conta_linha == conta_coluna:
        return True
    else:
        return False