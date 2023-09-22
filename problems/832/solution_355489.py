def eh_quadrada (matriz):
    """Função que, dada uma matriz de entrada, identifica se ela é quadrada ou não.
    Entrada: lista
    Saída: bool"""

    if len(matriz) > 0:
    	if len(matriz) == len(matriz[0]):
        	return True
        else:
            return False
    else:
        return False