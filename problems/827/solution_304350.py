def qtd_divisores(n):
	contador = 0
	for num in range(1, n+1):
		if n % num == 0:
			contador += 1
	return contador