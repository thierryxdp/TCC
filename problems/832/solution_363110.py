def eh_quadrada(matriz):
    """A função recebe uma matriz (lista) e retorna True se for 
    quadrada e False caso não seja."""
    for i in matriz:
    	if len(matriz) == len(matriz[i]):
            return True
        else:
            return False