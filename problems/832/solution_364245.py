def eh_quadrada (matriz):
    '''
    função que identidica e uma matriz é quadrada
    list->bool
    '''
    linha = len(matriz)
    coluna = len(matriz[0]) 
    for x in matriz:
        x = 0
        if linha == coluna:
            return True
        elif linha == coluna == []:
            return True      
        else:
            return False