def eh_quadrada(matriz):
    """ função que define de acordo com uma matriz recebida, se a mesma é quadrada ou não
    	entrada: lista
        saída: booleano, str
    """
    if len(matriz) == len(matriz[0]) and matriz == []:
            return True
    else:
        return False