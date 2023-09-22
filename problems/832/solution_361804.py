def eh_quadrada(matriz):
    """
    	Função que identifica se uma matriz é quadrada ou 
        não.
        list(list) -> bool
    """
	nlinhas = len(matriz)
    for linha in matriz:
        if not linha:
            return False