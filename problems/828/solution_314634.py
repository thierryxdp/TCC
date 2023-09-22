def primo(numero):
    ''' Dado um numero inteiro positivo, retorna 
    se ele é primo ou nao'''
    for x in range(1, numero-1):
        if numero % x == 0:
            return True
	return False