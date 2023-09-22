def pares(n):
    """
    str->tupla
    :param n: tupla com quatro elementos
    :param p: numeros pares
    :param return: Retorna os numeros pares da tupla
    """
    if n % 2 == 0:
    	return True
    else:
    	return False

def filtra_pares(a):    
    return tuple(filter(par,a))