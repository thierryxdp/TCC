def eh_quadrada(matriz):
    '''Função que recebe uma matriz e retorna se é uma matriz quadrada
    ou não (True ou Falso)
    list -> bool
    '''
    nlin = len(matriz)
    if nlin == 0:
        return True
    elif nlin == len(matriz[0]) :
        return True
    elif nlin != len(matriz[0]):
        return False