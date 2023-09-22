def eh_quadrada(matriz):
    """A função recebe uma matriz (lista) e retorna True se for 
    quadrada e False caso não seja."""
    if matriz == []:
        return True
    for linha in matriz:
        if len(linha) == len(matriz):
        	return True
        else:
        	return False