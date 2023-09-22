#Questao1
def eh_quadrada (matriz):
    '''
    A função informa se a matriz é
    quadrada ou não.
    list -> bool
    '''

    if matriz == [[]]:
        return True
    	linhas = len(matriz)
    	colunas = len(matriz[0])
    	if linhas == colunas:
        	return True
    	else:
        	return False