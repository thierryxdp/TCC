def primo(numero):
	"""Esta função verifica se o número é primo 
	int -> bool"""
	for i in range(2,numero):
		if numero % i == 0:
			return False
	else: 
		return True