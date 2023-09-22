def eh_quadrada(matriz):
    '''Função que diz se a matriz de entrada é quadrada ou não. 
    Retorna True se for quadrada, caso contrário retorna False
    list -> bool'''
    if type(matriz) == list:
        if matriz == [] or len(matriz) == len(matriz[0]):
            return True
        return False