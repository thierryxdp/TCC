#Questao1
def eh_quadrada (matriz):
    '''
    A função informa se a matriz é
    quadrada ou não.
    list -> bool
    '''
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    if linhas == 1:
        return True
    elif linhas == colunas:
        return True
    else:
        return False