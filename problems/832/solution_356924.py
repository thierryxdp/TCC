def eh_quadrada(matriz):
    """essa função, dada uma matriz, identifica se é quadrada ou não
	 utilizando uma função booleana
    list -> bool"""
    for linha in matriz:
        for coluna in linha:
            if coluna == []:
                return True
	else:
        return False