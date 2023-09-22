def primo(n):
    '''---'''
    
    indice = 0

	for count in range(2, n):
   		if (n % count == 0):
        	indice += 1

	if indice == 0:
        return True
    else:
        return False