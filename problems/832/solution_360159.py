def eh_quadrada(matriz):
    """ Função que retorna a situação do quadrado de uma matriz: list-> boolean"""
	
    if matriz == []:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False