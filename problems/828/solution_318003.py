def primo(numero):
	"""
	retorna se é verdadeiro ou falso que n é primo
	int->bool
	"""
	contador = 0
	for elemento in range(2, numero):
		if numero % elemento == 0:
			contador += 1
	if contador > 0:
		return False
	else:
		return True