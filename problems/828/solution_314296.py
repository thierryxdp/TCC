def primo(n):
	'''Função que dado um numero inteiro positivo, verifica se ele é primo ou não. Caso seja, a função irá retornar True, do contrario, False.'''
	'''int -> bool'''
	num = 0
	for numeros in range(1, n+ 1):
		if n % numeros == 0:
			num += 1
	if num > 2:
		return False
	else:
        return True