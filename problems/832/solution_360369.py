def eh_quadrada(matriz):
    '''função que retorna se uma matriz é quadrada.
    list -> bool'''
    qtdLinha = len(matriz)
    if qtdLinha > 0:
    	qtdColuna = len(matriz[0])
    	return qtdLinha == qtdColuna
    else:
        return True