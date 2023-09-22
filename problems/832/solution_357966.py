def eh_quadrada(matriz):
    '''Função que dada uma matriz retorna True se ela for quadrada ou False
caso ela não seja uma matriz quadrada.
list -> bool'''
    if len(matriz) == len(matriz[0]):
        return True
    elif matriz == []:
        return True
    else:
        return False