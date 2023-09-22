def eh_quadrada(matriz):
    ''' Essa funcao nos diz se uma matriz e quadrada;int->bool'''
    if len(matriz)== len(matriz[0]):
        return True
    if matriz==[]:
       return True
    else:
        return False