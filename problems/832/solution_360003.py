#Questão 1
def eh_quadrada(matriz):
    """Função que define se uma matriz é quadrada ou não,
    True para sim e False para não;
    list -> bool"""
    if len(matriz)==0:
    	return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False