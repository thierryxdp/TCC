#Exercício_01:
''' Essa função diz se a matriz recebida como entrada é quadrada ou não. '''
''' list ---> bool. '''

def eh_quadrada(matriz):
    nlin = len(matriz)+1
    ncol = len(matriz[0])+1
    if ncol == nlin:
        return True
    else:
        return False