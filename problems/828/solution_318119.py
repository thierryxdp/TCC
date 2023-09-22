#dado um número int positivo verifica se ele é primo
#int-->bool
def primo(n):
	for y in range(2,n):
    	if (n % y == 0):
        	return False
        else:
			return True