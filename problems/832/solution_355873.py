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
    elif linhas == len(matriz[0]):
        return True
    else:
        return False