def eh_quadrada(matriz):
    '''função que retorna se uma matriz é quadrada.
    list -> bool'''
    qtdLinha = len(matriz)
    qtdColuna = len(matriz[0])
    if qtdLinha > 0:
    	return qtdLinha == qtdColuna
    else:
        return True