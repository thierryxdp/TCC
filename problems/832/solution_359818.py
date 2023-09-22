def eh_quadrada(matriz):
    """ Retorna se a matriz passada como parâmetro é quadrada.
	list -> bool
	"""
	if(len(matriz) == 0): return True
    return len(matriz) == len(matriz[0])