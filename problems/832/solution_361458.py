def eh_quadrada (m):
    '''identifica se a matriz de entrada possui o mesmo elemento de linhas e colunas, e retorna True ou False'''
    '''list->bool'''
    if len(m) == 0:
        return True
    if len(m)==len(m[0]):
        return True
    else:
        return False