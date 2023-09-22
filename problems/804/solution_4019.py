#Start your python function here
#int, int, int, int --> int
def filtra_pares(tupla):
    """Agrupa somente os elementos pares provenientes dos parâmetros na 
       mesma ordem em que se encontravam.
       Dados de entrada: tupla --> possuindo vários números inteiros"""
    if tupla[0] % 2 == 0:
    	return tupla[0]
    elif tupla[1] % 2 == 0:
    	return tupla[1]
    elif tupla[2] % 2 == 0:
    	return tupla[2] 
    elif tupla [3] % 2 == 0:
    	return tupla[3]