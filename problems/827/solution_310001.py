def qtd_divisores(n):
	"""
	da o numero de divisores de n
	int->int
    """
	count = 0
	for numero in range(1, n):
		if n % elemento == 0:
			count=count+1
	if n < 0:
		return count
	else:
		return count + 1