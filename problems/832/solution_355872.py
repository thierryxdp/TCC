#Questao1
def eh_quadrada (matriz):
    '''
    A função informa se a matriz é
    quadrada ou não.
    list -> bool
    '''
    linhas = len(matriz)
    
    if matriz == [[]]:
        return True
    	colunas = len(matriz[0])
    elif linhas == colunas:
        return True
    else:
        return False