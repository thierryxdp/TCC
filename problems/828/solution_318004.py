def primo(n):
	"""
	retorna se é verdadeiro ou falso que n é primo
	int->bool
	"""
	count = 0
	for numero in range(2, n):
		if n % numero == 0:
			count=count+1
	if count > 0:
		return False
	else:
		return True