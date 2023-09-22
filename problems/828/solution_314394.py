def primo(n):
    '''Função que retorna a primalidade de "n" de entrada: int -> boolean'''
    
    indice = 0

	for numeros in range(2, n):
   		if (n % numeros == 0):
        	indice += 1

	if indice == 0:
        return True
    else:
        return False