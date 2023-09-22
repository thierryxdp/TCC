def eh_quadrada(matriz):
    '''Função que dada uma matriz retorna True se ela for quadrada ou False
caso ela não seja uma matriz quadrada.
list -> bool'''
    if matriz == []:
        return True
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False