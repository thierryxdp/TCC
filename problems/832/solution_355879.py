#Questão1
def eh_quadrada (matriz):
    '''
    A função informa se a matriz é
    quadrada ou não.
    list -> bool
    '''
    linhas = len(matriz)
    colunas = len(matriz[0])
    if matriz != [[]]:
        if linhas == colunas:
            return True
        else:
            return False            
    else:
        return True