def eh_quadrada (matriz):
    """Recebe uma matriz, testa se ela possui o mesmo número
    de linhas e colunas, e retorna um valor booleano se isso
    for verdade.
    list -> bool"""
    if matriz == [] or len(matriz) == len(matriz[0]):
	        return True
    else:
	        return False