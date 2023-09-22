def eh_quadrada(matriz):
    '''função que retorna se uma matriz é quadrada.
    list -> bool'''
    qtdLinha = len(matriz)
    qtdColuna = len(matriz[0])
    return qtdLinha == qtdColuna