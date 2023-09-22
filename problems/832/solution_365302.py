def eh_quadrada(matriz):
    '''Identifica se uma matriz é quadrada'''
    '''list-bool'''
    linha=[]
    for i in matriz:
        coluna=len(matriz[0])
        if linha==coluna and coluna==linha:
            return True
        else:
            return False