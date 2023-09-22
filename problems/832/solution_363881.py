def eh_quadrada(matriz):
    '''Função que pega a matriz de entrada, e verifica se ela é uma  matriz quadrada. Retornando
    uma valor booleano
    list,list→bool'''
    if matriz == []:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False