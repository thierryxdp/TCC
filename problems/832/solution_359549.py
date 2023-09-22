def eh_quadrada(matriz):
    '''Identifica se uma matriz e quadrada
    list -> bool'''
    
    n_linha=len(matriz)
    n_col=len(matriz[0])
    
    if n_linha==n_col or n_linha==0:
        return True
    else:
        return False