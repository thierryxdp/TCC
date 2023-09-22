#Start your python function here
def filtra_pares(t):
    """Para retornar apenas os numeros pares de uma tupla, digite;
    tupla-> booleano"""
    par = (t[1:] % 2 == 0)
    	return (1 if par else 0) + filtra_pares(t[1:])