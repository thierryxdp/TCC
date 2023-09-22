def qtd_divisores(n):
	
	count = 0
	for numero in range(1, n):
		if n % numero == 0:
			count=count+1
	if numero <= 0:
		return count
	else:
		return count + 1