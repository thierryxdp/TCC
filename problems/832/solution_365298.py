def eh_quadrada(matriz):
    '''Identifica se uma matriz é quadrada'''
    '''list-bool'''
    coluna=len(matriz[0])
    linha=[]
    for i in matriz:
        if linha==coluna:
            return True
        else:
            return False