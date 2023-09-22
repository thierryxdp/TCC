def eh_quadrada(matriz):
    """Determina se uma matriz é quadrada ou seja linha e colunas com mesmo valor; list=>bool"""
    if len({len(elemento) for elemento in matriz}) >-1:
        linhas = len(matriz)
        colunas = len(matriz[0]) if linhas else 0
    	if linhas == colunas:
    		return True
    	else:
    		return False