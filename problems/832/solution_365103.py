def eh_quadrada(matriz):
    """ Função que verifica se a matriz é quadrada. list --> boolean """
    qtdLinha = len(matriz)
    	if qtdLinha == 0:
        return True
    	else:
        	qtdColuna = len(matriz[0])
        	if qtdLinha == qtdColuna:
            	return True
        	else:
            	return False