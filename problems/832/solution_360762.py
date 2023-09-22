def eh_quadrada(matriz):
    '''função que dada uma matriz qualquer, retorna True se
    a matriz for quadrada e False caso cotrário
    list(list)--> bool'''
    if len(matriz) == 0:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else: 
        return False