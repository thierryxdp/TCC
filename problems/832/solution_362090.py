def eh_quadrada(matriz):
    """retorna True caso a matriz de entrada seja quadrada, caso não seja, retorna o valor booleano False,
    	(list) -> bool"""
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False