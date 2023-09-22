def eh_quadrada (matriz):
    '''função que identifica se uma matriz é quadrada, retorna
      True se for, False caso contrario.
      : list -> bool
    '''
    nlin = len(matriz)
    ncol = len(matriz[0])
    
    if nlin == ncol:
        return True
    elif nlin == 0:
        return True
    else:
        return False