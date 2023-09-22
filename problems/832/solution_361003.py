#Exercício_01:
''' Essa função diz se a matriz recebida como entrada é quadrada ou não. '''
''' list ---> bool. '''

def eh_quadrada(matriz):
    if matriz == []:
        return True
    else:
        nlin = len(matriz)
        ncol = len(matriz[0])
        if ncol == nlin:
            return True
        else:
            return False