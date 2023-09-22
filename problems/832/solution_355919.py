def eh_quadrada (matriz):
    """função booleana que identifica se uma matriz é quadrada.
    matriz->boolena"""
    if len(matriz)==0:
    	return True
    linha1=matriz[0]
    if len(linha1)==len(matriz):
        return True
    else:
        return False