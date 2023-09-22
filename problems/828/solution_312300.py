def primo(num):
	''''funcao verifica se numero dado eh primo (retorna True), ou nao (retorna False).
	int --> bln'''
	if num > 1:
		for i in range(2,num):
			if (num % i) == 0:
				return False
				break
		else:
			return True
	else:
		return False