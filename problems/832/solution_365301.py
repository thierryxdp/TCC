def eh_quadrada(matriz):
    '''Identifica se uma matriz é quadrada'''
    '''list-bool'''
    linha=[]
    coluna=len(matriz[0])
    for i in matriz:
        if linha==coluna and coluna==linha:
            return True
        else:
            return False