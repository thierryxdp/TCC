def eh_quadrada(matriz):
    """essa função, dada uma matriz, identifica se é quadrada ou não
	 utilizando uma função booleana True ou False, respectivamente
    list -> bool"""
    for linha in matriz:
        for coluna in linha:
            if coluna != []:
                return False

    else:
        return True