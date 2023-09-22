def primo(n):
	num = 0
	for numeros in list(range(1, n+ 1)):
		if n % numeros == 0:
			num += 1
	if num > 2:
		return False
	else:
		return True