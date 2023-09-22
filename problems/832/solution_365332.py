def eh_quadrada(matriz):
    '''Identifica se uma matriz é quadrada'''
    '''list-bool'''
    linha=[]
    coluna=[]
    for i in matriz:
        coluna=len(matriz[0])
        linha=len(matriz[0]]
        if linha==coluna:
            return True
        else:
            return False