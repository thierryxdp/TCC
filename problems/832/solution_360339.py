def eh_quadrada(matriz):
    '''Função que, dada uma matriz qualquer, retorna True se for quadrada ou False, caso contrário.
list(list) --> bool'''
    if matriz == []:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False