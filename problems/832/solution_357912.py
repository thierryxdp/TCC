'''Retorna se uma matriz é quadrada ou não'''
#list -> bool
def eh_quadrada(matriz):
    if matriz == []:
        return True
    elif len(matriz) == len(matriz[0]):
            return True
    else:
        return False