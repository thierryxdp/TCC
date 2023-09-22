def eh_quadrada (matriz):
    '''
    '''
    linha = len(matriz)
    coluna = len(matriz[0]) 
    for linha in matriz:
        if linha == coluna:
            return True
        elif linha == coluna == 0:
            return True      
        else:
            return False