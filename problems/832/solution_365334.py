def eh_quadrada(matriz):
    '''Identifica se uma matriz é quadrada'''
    '''list-bool'''
    coluna=[]
    for i in matriz:
        coluna=len(matriz[0])
        if linha==coluna:
            return True
        else:
            return False