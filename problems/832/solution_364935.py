def eh_quadrada(matriz):
    """ Função que retorne se uma matriz é quadrada ou não; list=>bool"""
    matriz = []
    for linha in matriz:
   		if matriz == []:
            return True
        if len(matriz) == len(matriz[0]):
            return True
        else: 
            return False